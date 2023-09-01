from utils import tlssession, getproxy
import organizer


class loginHelp:
    def __init__(self, username, password):
        self.proxy = getproxy.get_random_proxy()
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
        self.session.headers.update(self.headers)

    def login(self):
        res = self.session.post(self.login_api, data=self.payload, proxy=self.proxy, allow_redirects=True)
        g = str(res.text).split('name="csrf_token" value="')[1].split('">')[0]
        self.payload['csrf_token'] = g
        self.session.post(self.login_api, data=self.payload, proxy=self.proxy, allow_redirects=True)
        url = 'https://www.reddit.com/svc/shreddit/ptPzVvzFulwNDmL2eV'
        pay = {"csrf_token": g, "data": []}
        self.session.post(url, data=pay, proxy=self.proxy, allow_redirects=True)
        loid = ''
        xred = ''
        autho = ''
        for cookie in self.session.cookies:
            if cookie.name == 'loid':
                print('updating x-reddit-loid', cookie.value)
                loid = cookie.value
            if cookie.name == 'session_tracker':
                print('updating x-reddit-session', cookie.value)
                xred = cookie.value
            if cookie.name == 'token_v2':
                print('updating Bearer', cookie.value)
                autho = cookie.value
        if self.username in organizer.controlJson().current_content:
            organizer.controlJson().add_account_info(self.username)
        else:
            organizer.controlJson().add_account_info(self.username, password=self.password,
                                                     recaptcha_token='03ADUVZwCa-yv-PGcRBM2u_C3mcqX7IF5b5TQt8jU3lr5Xa5HB_JT1ZyjKyEvealf6RNLZisqMKAmEl6wc42lkyCE5NDuWZMbUJvZu4srcwbGv3oZJX2qacd5bcgL0UFFKz1t_d1XorrlbKd9Kg2HY0cVEIq3vx1HW25J9tXSpXBC3Zn0ocYfBVzCyd5sQhyp9E5h6zL9t7ucgukGdyFlpspNCw35W-q9_E9cNBCyNy74zEANRghxVd_oyfoBjkFyYjfXiMbnUM1TNibkfgd-1oGOnV6g5y8zs_XoLgNnBGt4zFkZyXPdS1yqRNhDkKoWKKSmDdCAWVujLcQ1zFWGeGchoCVm-zHgfmwPl-JzJABVn9y0NO8pvg9Dt3aLQGwIn8hpiVv5mkv52zWop9os09Ehvlp3Y4I4gOMZsExkBtOAio_1H3LKz2Y0J2P-UTQnDSI0DHPz9-Bpy8EIkQ4kXZeiRAq6ZuhalKTGM7u1dEG9TiAl4PMKxLWqoY_onLFwpp3K0hCT6BNu3jCz74wNUlYaWsTiprqHFFPRHQL83sbQydEX0nCUjTzPSsfJWtZB-JUbiWL0FPZ_pHxQvl-W7p5O3-jBc2z8weDxo24XJ4dGNZ4ZSquEjnZqzMp5MWffO6fpQKL0szr0YVwwR_ATNBlRqqd_uuloouog6m3Ul-XaWz_Apkmc_eZQPCGfP1p9Mcq8soNQB0ZZ_L2UlrjO9jaJqjr4s41k8jTVb_Eoi5wF2JE51GIjJFPOqmoqF-HQ7G7G_sl1jscbqVcqI5zAneyEoS9om5nAN5ClIhYFgTBvqTiEVvKo1-9Jr0GkV33TsU_4LgUT8i_rC14fNS7Dvnvq8tgmSGzZnJ4Bo-gyhSIDgFaq5fjBii3qDL6YyVaozQ6doWTQZ3ThTlnME3OnhtWNqppP55sAgHeHrvj2XjpvA1rp7mvdTPe1gC6rm8Zh_8Ap4ZRIbkEkiE3IuHjZGEiJjxRtVWZ5AAI-laOUuvo4INoqqU9AAR5zAzJw82telGSEokbUCI4DTCVQok8IJLtRGbyJyYpo1DC7tArFLDCN9-ZA-0Q_Scq3E5DaHFLU1MqWoP6SWNZ3HyGRam1xyEU9H-Yo8ltrPWf_kOe94FdUPCgpIPXIpxogSfW_mjfeCgkK7KoDtqloF8JxfSVeNlKh4L-tLxTG2miMq7Ozlen5eDyN_5VdDWbVkLxEa4Ssd4BhvEJ9fE5GwQwv6EXI3syJRF1HWHo8w_0CPWiLsuMr10v39ARiUjlLcnPL9RIz3LD93g_uxZ2J86GXoTcyQHjJ-tHANgBv11NGUUUuFL1y1rUSQP1WfjjB3J9U7eUHwRi_szzj-SHjC1r30NjmqJnNytoEl4N9IY_-edWbOvQh2LP-HdI7Lcr9Bn3iRJJL5v8ThVVSt8yg0RTnQSdfrr7qWy7hgNgjX-VWE6c7XfQGeWOZ5DTOkP_daL5EAqaKKw46Rf6bTwbPrcVIi4VTlVT8K89CUJ_b7sbRZX_ju4qZlJW5hooSxGcBkJtRvohXGY9Rce11lUhat',
                                                     x_reddit_loid=loid,
                                                     x_reddit_session=xred,
                                                     authorization=autho
                                                     )
