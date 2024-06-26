#!/usr/bin/python3
"""A script that takes a GitHub username and a token and returns the
associated user id"""
import requests
import sys


if __name__ == "__main__":
    token = sys.argv[2]
    username = sys.argv[1]
    headers = {"Authorization": f"Bearer {token}",
               "Accept": "application/json",
               "X-GitHub-Api-Version": "2022-11-28"}
    response = requests.post("https://api.github.com/user", headers=headers)
    true_username = response.json().get('login')
    name = response.json().get('name')
    if true_username == username or name == username:
        print(response.json()['id'])
    else:
        print("None")
