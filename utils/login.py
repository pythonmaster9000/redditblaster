from utils import tlssession
import organizer


class loginHelp:
    def __init__(self, username, password):
        self.session = tlssession.session
        self.username = username
        self.password = password
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
        self.session.headers.update(headers)

    def login(self):
        res = self.session.post(self.login_api, data=self.payload, allow_redirects=True)
        g = str(res.text).split('name="csrf_token" value="')[1].split('">')[0]
        self.payload['csrf_token'] = g
        self.session.post(self.login_api, data=self.payload, allow_redirects=True)
        url = 'https://www.reddit.com/svc/shreddit/ptPzVvzFulwNDmL2eV'
        pay = {"csrf_token": g, "data": []}
        self.session.post(url, data=pay, allow_redirects=True)
        for cookie in self.session.cookies:
            if cookie.name == 'loid':
                print('updating x-reddit-loid', cookie)
            if cookie.name == 'session_tracker':
                print('updating x-reddit-session', cookie)
            if cookie.name == 'token_v2':
                print('updating Bearer', cookie)
            if self.username in organizer.controlJson().current_content:
                organizer.controlJson().add_account_info(self.username)
            else:
                organizer.controlJson().add_account_info(self.username, password=self.password)
