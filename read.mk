# Reddit Blaster Instructions

## Adding Accounts

Add accounts via CLI with username/password or directly into the tokens.json file 
(no captcha support right now so the captcha token may stop working)
You can put the tokens/auth info in manually if you are logged into a reddit account and make a 
request (comment, etc) with the network tab open and copy the values from the "Request Headers".

## Posts

Follow prompt on CLI, posts require the subreddit title and content and will start a thread which will continue to post every x seconds.

## Comments

Same as posts except require the comment id, which is found in the URL of a post example:

https://www.reddit.com/r/SwipeHelper/comments/ ----- > 15gd0m8 < ----- /honest_profile_reviews_and_profile_guide_august/
