import organizer
from utils import comment, post, login
import threading
import time


def tokenRefresh():
    time.sleep(86400)
    print('refreshing after 24 hours')
    for user in organizer.controlJson().current_content:
        login.loginHelp(user, user['password'])


def taskHelp(seconds_to_wait, task_type, comment_content=None, post_to_comment=None, post_content=None, post_title=None, subreddit=None):
    if task_type == 'comment':
        while True:
            for user in organizer.controlJson().current_content:
                print('commenting', comment_content)
                comment.commentHelper(user, comment_content, post_to_comment).post_comment()
                time.sleep(seconds_to_wait)
    if task_type == 'post':
        while True:
            for user in organizer.controlJson().current_content:
                print('posting', post_title)
                post.postHelper(user, post_title, post_content, subreddit).post_post()
                time.sleep(seconds_to_wait)
    if task_type == 'refresh':
        print('refreshing accounts')
        for user in organizer.controlJson().current_content:
            login.loginHelp(user, user['password'])


if __name__ == "__main__":
    background_thread = threading.Thread(target=tokenRefresh)
    background_thread.start()
    while True:
        print('1. Add user')
        print('2. Schedule comment on post')
        print('3. Schedule post')
        f = input('Choose number ')
        if f == '1':
            info = input('input username password (format: username password)')
            info = info.split()
            login.loginHelp(info[0], info[1]).login()
        if f == '2':
            info = input('input number of seconds per comment cycle')
            comment_cycle = int(info)
            info = input('input comment content')
            comment_content = info
            info = input('input post id')
            postid = info
            background_thread = threading.Thread(target=taskHelp, args=(comment_cycle, 'comment'), kwargs={'comment_content' : comment_content, 'post_to_comment' : postid})
            background_thread.start()
        if f == '3':
            info = input('input number of seconds per comment cycle')
            post_cycle = int(info)
            info = input('input post subreddit')
            subreddit = info
            info = input('input post title')
            title = info
            info = input('input post content')
            content = info
            background_thread = threading.Thread(target=taskHelp, args=(post_cycle, 'post'), kwargs={'post_content': content, 'post_title': title, 'subreddit' : subreddit})
            background_thread.start()
