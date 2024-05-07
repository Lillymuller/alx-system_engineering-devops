#!/usr/bin/python3
"""
Returns Query Reddit API for number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "Mozilla/5.0"
            }
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json().get("data").get("subscribers")
    else:
        return 0
