import organizer
from utils import comment

if __name__ == "__main__":
    while True:
        f = input("Comment as test user?: y")
        if f == "y":
            print(comment.commentHelper('testacc', 'hello dawg').post_comment())
