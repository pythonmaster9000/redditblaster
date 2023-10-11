import tlssession
import requests as r
import json
import time
import advanced


class RedditBot:
    def __init__(self, username, password, proxy, sitekey):
        self.sitekey = sitekey
        self.session = tlssession.session
        self.username = username
        self.password = password
        self.proxy = self.format_proxy(proxy)
        self.login_api = 'https://www.reddit.com/login'
        self.payload = {
            'app_name': 'web3x',
            'csrf_token': '2b0d75c1bb2a0c5043846708a3c430d8e63aadab',
            'otp': '',
            'password': self.password,
            'dest': 'https://www.reddit.com',
            'username': self.username,
        }
        self.headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "Referer": "https://www.reddit.com/account/login/?experiment_d2x_safari_onetap=enabled&experiment_d2x_google_sso_gis_parity=enabled&experiment_d2x_am_modal_design_update=enabled&experiment_mweb_sso_login_link=enabled&shreddit=true&use_accountmanager=true",
            "Referrer-Policy": "strict-origin-when-cross-origin"
        }
        self.session.headers.update(self.headers)

    def format_proxy(self, proxy):
        splitted = proxy.split(':')
        return f'http://{splitted[2]}:{splitted[3]}@{splitted[0]}:{splitted[1]}'

    def login(self):
        res = self.session.post(self.login_api, data=self.payload, allow_redirects=True)
        print(res.status_code)
        g = str(res.text).split('name="csrf_token" value="')[1].split('">')[0]
        self.payload['csrf_token'] = g
        self.session.post(self.login_api, data=self.payload, allow_redirects=True)
        url = 'https://www.reddit.com/svc/shreddit/ptPzVvzFulwNDmL2eV'
        pay = {"csrf_token": g, "data": []}
        self.session.post(url, data=pay, proxy=self.proxy, allow_redirects=True)
        cock = []
        for cookie in self.session.cookies:
            cock.append(vars(cookie))
        advanced_result = advanced.advance_auth(cock)
        self.reddit_loid = advanced_result.get('x-reddit-loid')
        self.reddit_session = advanced_result.get('x-reddit-session')
        self.authorization = advanced_result.get('authorization')

    def get_captcha(self):
        capmonster_payload = {
            "clientKey": "d36e45d8bf295b976a6816ca70a5163a",
            "task":
                {
                    "type": "RecaptchaV2EnterpriseTask",
                    "websiteURL": f"https://www.google.com/recaptcha/enterprise/reload?k=6LfRNvoUAAAAAKgEWIXbpPkMWcboc1n1gAeXq7lP",
                    "websiteKey": "6LeTnxkTAAAAAN9QEuDZRpn90WwKk_R1TRW_g-JC",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
                }
        }
        res = r.post("https://api.capmonster.cloud/createTask", json=capmonster_payload)
        capmonster_taskid = res.json()["taskId"]
        getresultpay = {
            "clientKey": "d36e45d8bf295b976a6816ca70a5163a",
            "taskId": capmonster_taskid
        }
        while True:
            time.sleep(1)
            res = r.post("https://api.capmonster.cloud/getTaskResult", json=getresultpay).json()
            print(res)
            if res['status'] == 'ready':
                print('cap ready')
                print(res["solution"]["gRecaptchaResponse"])
                return res["solution"]["gRecaptchaResponse"]

    def post_submission(self, title, content, subreddit):
        headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "authorization" : self.authorization,
            "content-type": "application/x-www-form-urlencoded",
            "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "x-reddit-loid" : self.reddit_loid,
            "x-reddit-session" : self.reddit_session,
            "Referer": "https://www.reddit.com/",
            "Referrer-Policy": "origin-when-cross-origin"
        }
        payload = {
            'sr': subreddit,
            'submit_type': 'subreddit',
            'api_type': 'json',
            'show_error_list': True,
            'title': title,
            'spoiler': False,
            'nsfw': False,
            'recaptcha_token': self.get_captcha(),
            'kind': 'self',
            'original_content': False,
            'post_to_twitter': False,
            'sendreplies': True,
            'richtext_json': {
                "document": [{"e": "par", "c": [{"e": "text", "t": content}]}]},
            'validate_on_submit': True,
        }

        url = 'https://oauth.reddit.com/api/submit?resubmit=true&redditWebClient=desktop2x&app=desktop2x-client-production&rtj=only&raw_json=1&gilding_detail=1'

        res = self.session.post(
            url,
            headers=headers,
            data=payload
            # proxy=self.proxy
        )
        print(res.text)
        return res


if __name__ == "__main__":
    input()
    bot = RedditBot('akamadogi3', '8l7yimkndb', '161.123.129.98:5431:bxjuynuk:223uy72sflzw',
                    '6LfRNvoUAAAAAKgEWIXbpPkMWcboc1n1gAeXq7lP')
    bot.login()
    time.sleep(5)
    bot.post_submission('I enjoy penuts!', "peanutsss YUMMERs", 'peanutlovers')
