#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import requests
import sys

def number_of_subscribers(subreddit):
    '''Reddit API URL for getting subreddit information'''
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    "Set a custom User-Agent to avoid Too Many Requests error"
    headers = {'User-Agent': 'by /u/bensonmm'}

    try:
        "Make a GET request to the Reddit API"
        response = requests.get(url, headers=headers)

        "Check if the request was successful (status code 200)"
        if response.status_code == 200:
            '' Parse the JSON response"
            subreddit_info = response.json()

            "Extract and return the number of subscribers"
            return subreddit_info['data']['subscribers']
        elif response.status_code == 404:
            "If subreddit is not found, return 0"
            return 0
        else:
            "If there's an error, print the status code and return 0"
            print(f"Error: {response.status_code}")
            return 0
    except Exception as e:
        "Print the exception and return 0"
        print(f"Exception: {e}")
        return 0

if __name__ == "__main__":
    "Check if the correct number of command-line arguments is provided"
    if len(sys.argv) != 2:
        print("Usage: python script_name.py subreddit_name")
        sys.exit(1)

    "Get subreddit name from command-line arguments"
    subreddit_name = sys.argv[1]

    "Call the function and print the result"
    subscribers_count = number_of_subscribers(subreddit_name)
    if subscribers_count > 0:
        print(f"The subreddit /r/{subreddit_name} has {subscribers_count} subscribers.")
    else:
        print(f"The subreddit /r/{subreddit_name} is not valid or doesn't exist.")
