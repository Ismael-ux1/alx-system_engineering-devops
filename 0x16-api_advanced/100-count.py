#!/usr/bin/python3
"""
function that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""
from collections import Counter
import re
import requests


def count_words(subreddit, word_list, word_counts=None, after=None):
    """Recursively queries Reddit for keyword counts in hot articles."""
    if word_counts is None:
        word_counts = Counter()

    # Reddit API endpoint for getting hot articles
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Include 'after' parameter to paginate through results
    params = {'limit': 10, 'after': after}

    try:
        # Send a GET request to the API
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        # Check if the subreddit is valid or if an error occurred
        if response.status_code != 200:
            return

        # Parse the JSON response
        data = response.json()
        articles = data.get('data', {}).get('children', [])

        # Extract article titles from this page
        titles = [article['data']['title'] for article in articles]

        # Count occurrences of keywords in titles
        for title in titles:
            for keyword in word_list:
                keyword = keyword.lower()  # Convert to lowercase
                # Use regex to find whole words and avoid partial matches
                matches = re.findall(rf'\b{re.escape(keyword)}\b',
                                     title, re.IGNORECASE)
                word_counts[keyword] += len(matches)

        # Check if there are more pages (using the 'after' parameter)
        after = data.get('data', {}).get('after')
        if after:
            # Make a recursive call with the 'after' parameter
            count_words(subreddit, word_list, word_counts, after=after)
        else:
            # No more pages, print the sorted counts
            sorted_counts = sorted(word_counts.items(), key=lambda x:
                                   (-x[1], x[0]))
            for keyword, count in sorted_counts:
                print(f"{keyword}: {count}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
