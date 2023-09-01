import json


class controlJson:
    def __init__(self):
        with open("tokens.json", 'r') as file:
            self.current_content = json.load(file)

    def add_account_info(self, username, recaptcha_token, authorization, x_reddit_loid, x_reddit_session):
        self.current_content[username] = {
            "recaptcha_token": recaptcha_token,
            "authorization": authorization,
            "x-reddit-loid": x_reddit_loid,
            "x-reddit-session": x_reddit_session
        }
        with open("tokens.json", 'w') as outfile:
            json.dump(self.current_content, outfile, indent=4)
