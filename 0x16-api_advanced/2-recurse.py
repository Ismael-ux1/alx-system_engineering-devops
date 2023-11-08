#!/usr/bin/python3
import requests

"""
A function that queries the Reddit API and
returns titles of all hot articles
"""


def recurse(subreddit, hot_list=[], after=None):
    # Define the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Define the headers for the request
    headers = {'User-agent': 'Mozilla/5.0'}

    # Define the parameters for the request
    params = {'after': after}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # If the subreddit is not valid, return None
    if response.status_code != 200:
        return None

    # Parse the JSON response
    data = response.json()

    # Extract the titles of the hot articles and append them to the hot_list
    for post in data['data']['children']:
        hot_list.append(post['data']['title'])

    # Get the ID of the last article on the current page
    after = data['data']['after']

    # If there are more pages of results,
    # recursively call the function to fetch the next page
    if after is not None:
        return recurse(subreddit, hot_list, after)

    # If there are no more pages of results, return the hot_list
    return hot_list
