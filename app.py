import json
import sys
import os
import doctest
import csv
from datetime import date

import twitter
from t import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET

class MyClass:
    """A simple testing class with two parameters."""
    def __init__(self, str):
        self.strg = str
    
    def rev(self, s):
        """A simple testing method.
        >>> x = MyClass('ahoj')
        >>> x.rev('ahoj')
        joha
        """
        for i in range(len(s)-1, -1, -1):
            print(s[i], end='')

# x = 3.15487
# print(x.as_integer_ratio())
# print(x.hex())


original = {'flour':630, 'sugar':15, 'salt':10, 'yeast':10, 'olive oil':32, 'water':420}
print('Original grams:', original)

p = 500/630
print('Ratio: ', p)

portioned = {}
for k,v in original.items():
    portioned[k] = round(v*p)
    # portioned.append(k, round(v*k))

# portioned = {x: x*p for x in original.items()}
print("Portioned grams: ", portioned)

# Create an Api instance.
# api = twitter.Api(consumer_key=CONSUMER_KEY,
#                   consumer_secret=CONSUMER_SECRET,
#                   access_token_key=ACCESS_TOKEN_KEY,
#                   access_token_secret=ACCESS_TOKEN_SECRET)

# users = api.GetFriends()
# tweets = api.GetUserTimeline(user_id=196700354, count=200)

# with open("tweets.json", "w") as f:
#     for tweet in tweets:
#         # f.write(json.dumps(tweet.text))
#         f.write(json.dumps(tweet._json))
#         f.write("\n")

# print([u.screen_name for u in users])