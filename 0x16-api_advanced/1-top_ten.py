#!/usr/bin/python3
"""
A function that queries the Reddit API and,
prints the titles of the forst 10 hot post.
"""
import requests


def top_ten(subreddit):
    """ define the fonction that takes a subreddit as an argument """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # set the header for the request
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Send a GET request to the Reddit API's
    response = requests.get(url, headers=headers, allow_redirects=False)

    # if it's 200 the function prints None and returns
    if response.status_code != 200:
        print(None)
        return

    # parse the JSON response to extract the posts
    data = response.json()

    # Loop through the posts and print the title of each post
    for post in data['data']['children']:
        print(post['data']['title'])
