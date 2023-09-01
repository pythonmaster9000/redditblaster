from utils import tlssession
import json


class AccountError(Exception):
    """Account not in tokens.json"""
    pass


class postHelper:
    def __init__(self, account_name, post_title, post_content, subreddit):
        with open(r'tokens.json', 'r') as f:
            account_info = json.load(f)
        try:
            self.account = account_info[account_name]
        except KeyError:
            raise AccountError()
        self.session = tlssession.session
        self.title = post_title
        self.subreddit = subreddit
        self.content = post_content
        self.recaptcha_token = self.account['recaptcha_token']
        self.authorization = self.account['authorization']
        self.x_reddit_loid = self.account['x-reddit-loid']
        self.x_reddit_session = self.account['x-reddit-session']
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
        self.payload = {
            'sr': self.subreddit,
            'submit_type': 'subreddit',
            'api_type': 'json',
            'show_error_list': True,
            'title': self.title,
            'spoiler': False,
            'nsfw': False,
            'recaptcha_token': self.recaptcha_token,
            'kind': 'self',
            'original_content': False,
            'post_to_twitter': False,
            'sendreplies': True,
            'richtext_json': {
                "document": [{"e": "par", "c": [{"e": "text", "t": self.content}]}]},
            'validate_on_submit': True,
        }

        self.url = 'https://oauth.reddit.com/api/submit?resubmit=true&redditWebClient=desktop2x&app=desktop2x-client-production&rtj=only&raw_json=1&gilding_detail=1'

    def post_post(self):
        res = self.session.post(
            self.url,
            headers=self.headers,
            data=self.payload
        )
        print(res)
        return res
