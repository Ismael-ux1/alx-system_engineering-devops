#!/usr/bin/python3
""" A function that queries the Reddit API and returns no_ subcribers """
import requests


def number_of_subscribers(subreddit):
    """ define the function that takes a subreddit as argument """
    # set header for the request
    headers = {'User-Agent': 'custom'}
    # send a GET request to the Reddit API's
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                            headers=headers, allow_redirects=False)
    """
    check the status code of the response
    If it's not 200, the function returns 0.
    """
    if response.status_code != 200:
        return 0
    """
    If the request is succesful,
    parse the JSON response to extract and return the number of subscribers
    """
    return response.json()['data']['subscribers']
