#!/usr/bin/python3
"""
A function that queries the Reddit API and
returns titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    if hot_list is None:
        hot_list = []
    # Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Define the headers for the request
    headers = {'User-agent': 'Mozilla/5.0'}

    # Define the parameters for the request
    params = {'limit': 10, 'after': after}

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        # If the subreddit is not valid, return None
        if response.status_code != 200:
            return None

        # Parse the JSON response
        data = response.json()
        articles = data.get('data', {}).get('children', [])

        # Extract the titles from this page
        titles = [article['data']['title'] for article in articles]

        # Append the titles to the hot_list
        hot_list.extend(titles)

        # Check if there are more pages (using the 'after' parameter)
        after = data.get('data', {}).get('after')
        if after:
            # Make a recursive call with the 'after' parameter
            return recurse(subreddit, hot_list, after=after)
        else:
            # No more pages, return the final list of titles
            return hot_list

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
