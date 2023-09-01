from utils import tlssession
import json


class AccountError(Exception):
    """Account not in tokens.json"""
    pass


class commentHelper:
    def __init__(self, account_name, comment, post_id):
        with open(r'tokens.json', 'r') as f:
            account_info = json.load(f)
        try:
            self.account = account_info[account_name]
        except KeyError:
            raise AccountError()
        self.post_id = post_id
        self.recaptcha_token = self.account['recaptcha_token']
        self.authorization = self.account['authorization']
        self.x_reddit_loid = self.account['x-reddit-loid']
        self.x_reddit_session = self.account['x-reddit-session']
        # TODO thing_id is the comment id shown in url
        self.payload = {
            'api_type': 'json',
            'return_rtjson': 'true',
            'thing_id': f't3_{post_id}',
            'recaptcha_token': self.recaptcha_token,
            'text': comment,
            'richtext_json': {"document": [{"e": "par", "c": [{"e": "text", "t": comment}]}]}
        }
        self.headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "authorization": self.authorization,
            "content-type": "application/x-www-form-urlencoded",
            "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "x-reddit-loid": self.x_reddit_loid,
            "x-reddit-session": self.x_reddit_session,
            "Referer": "https://www.reddit.com/",
            "Referrer-Policy": "origin-when-cross-origin"
        }
        self.url = 'https://oauth.reddit.com/api/comment.json?rtj=only&emotes_as_images=true&redditWebClient=desktop2x&app=desktop2x-client-production&raw_json=1&gilding_detail=1'
        self.session = tlssession.session

    def post_comment(self):
        res = self.session.post(
            self.url,
            headers=self.headers,
            data=self.payload
        )
        print(res)
        return res
