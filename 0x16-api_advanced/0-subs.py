#!/usr/bin/python3
"""
Importing requests module
"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json' 
     # Using f-string for better readability
    response = requests.get(url, headers=user_agent)

    if response.status_code != 200:
        return 0  # Return 0 if the request was not successful

    all_data = response.json()

    try:
        return all_data['data']['subscribers']
    except KeyError:
        return 0  # Return 0 if the key is not found in the response JSON