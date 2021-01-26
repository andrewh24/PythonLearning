import json
import sys

import twitter
from t import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET

# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET)

# users = api.GetFriends()
tweets = api.GetUserTimeline(user_id=196700354, count=200)

with open("tweets.json", "w") as f:
    for tweet in tweets:
        # f.write(json.dumps(tweet.text))
        f.write(json.dumps(tweet._json))
        f.write("\n")

# print([u.screen_name for u in users])