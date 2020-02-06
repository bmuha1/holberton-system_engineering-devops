#!/usr/bin/python3
"""
Query the Reddit API and return a lit containing the titles of all hot
articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    try:
        r = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.
                         format(subreddit, after),
                         headers={'User-Agent': 'custom'},
                         allow_redirects=False)
        if after is None:
            return hot_list
        for thread in r.json().get('data').get('children'):
            hot_list += [thread.get('data').get('title')]
        after = r.json().get('data').get('after')
        recurse(subreddit, hot_list, after)
        return hot_list
    except:
        return None
