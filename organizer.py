import json


class controlJson:
    def __init__(self):
        with open("tokens.json", 'r') as file:
            self.current_content = json.load(file)

    def add_account_info(self, username, recaptcha_token=None, authorization=None, x_reddit_loid=None, x_reddit_session=None, password=None):
        if username in self.current_content:
            self.current_content[username] = {
                "password" : self.current_content[username]['password'],
                "recaptcha_token": recaptcha_token if recaptcha_token else self.current_content[username]['recaptcha_token'],
                "authorization": authorization if authorization else self.current_content[username]['authorization'],
                "x-reddit-loid": x_reddit_loid if x_reddit_loid else self.current_content[username]['x-reddit-loid'],
                "x-reddit-session": x_reddit_session if x_reddit_session else self.current_content[username]['x-reddit-session']
            }
        else:
            self.current_content[username] = {
                "password": password,
                "recaptcha_token": recaptcha_token,
                "authorization": authorization,
                "x-reddit-loid": x_reddit_loid,
                "x-reddit-session": x_reddit_session
            }
        with open("tokens.json", 'w') as outfile:
            json.dump(self.current_content, outfile, indent=4)


