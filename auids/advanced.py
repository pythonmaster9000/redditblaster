from seleniumwire.undetected_chromedriver import Chrome
from undetected_chromedriver import ChromeOptions

def advance_auth(cookies):
    options = ChromeOptions()

    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = Chrome(options=options)
    for c in cookies:
        if "sameSite" in c:
            c['sameSite'] = 'Strict'
    driver.get('https://www.reddit.com/r/SwipeHelper/')
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    driver.get('https://www.reddit.com/r/SwipeHelper/comments/16874gd/honest_profile_reviews_and_profile_guide/')
    driver.implicitly_wait(5)
    f = driver.requests
    for req in f:
        for i in req.headers.values():
            if i.startswith('Bearer'):
                correct = req.headers
                driver.close()
                return correct
