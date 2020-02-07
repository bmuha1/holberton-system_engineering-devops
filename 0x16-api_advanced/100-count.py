#!/usr/bin/python3
"""
Query the Reddit API, parse the titles of all hot articles for a given
subreddit, and print a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=''):
    try:
        r = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.
                         format(subreddit, after),
                         headers={'User-Agent': 'custom'},
                         allow_redirects=False)
        if after is None:
            dict = {}
            for word in word_list:
                for hot_word in hot_list:
                    if word == hot_word:
                        if word not in dict:
                            dict[word] = 1
                        else:
                            dict[word] += 1
            for word in sorted(dict, key=dict.get, reverse=True):
                if dict[word]:
                    print('{}: {}'.format(word, dict[word]))
            return hot_list
        for thread in r.json().get('data').get('children'):
            hot_list += thread.get('data').get('title').lower().split()
        after = r.json().get('data').get('after')
        count_words(subreddit, word_list, hot_list, after)
        return hot_list
    except:
        return None
