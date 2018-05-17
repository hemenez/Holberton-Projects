#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    print(subreddit)
    url = 'https://www.reddit.com/r/' + subreddit + '/about'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    print(response.json())
