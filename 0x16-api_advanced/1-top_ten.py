#!/usr/bin/python3
"""
Query the Reddit API and return the titles of the first 10 hot posts listed
for a given subreddit
"""
import requests


def top_ten(subreddit):
    try:
        r = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.
                         format(subreddit),
                         headers={'User-Agent': 'custom'},
                         allow_redirects=False)
        for thread in r.json().get('data').get('children'):
            print(thread.get('data').get('title'))
    except:
        print('None')
