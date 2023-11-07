#!/usr/bin/python3
"""
A function that queries the Reddit API and,
prints the titles of the forst 10 hot post.
"""
import requests


def top_ten(subreddit):
    """ define the fonction that takes a subreddit as an argument """

    # set the header for the request
    headers = {'User-Agent': 'custom'}

    # Send a GET request to the Reddit API's
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10' \
          '?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)

    # check if the status code of the response
    # if it's 200 the function prints None and returns
    if response.status_code != 200:
        print(None)
        return

    # if the request is sucessful, parse the JSON response to extract the posts
    posts = response.json()['data']['children']

    # Loop through the posts and print the title of each post
    for post in posts:
        print(post['data']['title'])
