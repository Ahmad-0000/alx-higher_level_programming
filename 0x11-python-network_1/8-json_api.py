#!/usr/bin/python3
"""A script that takes a URL and a letter as a paremeter, sends it
to a server and handles JSON response bodies"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    letter = {'q': ""}
    if len(sys.argv) > 1:
        letter['1'] = sys.argv[2]
    response = requests.post(url, data=letter)
    try:
        json_dict = response.json()
        print(f'[{json_dict["id"]}] {json_dict["name"]}')
    except Exception:
        if not response.text:
            print('No result')
        else:
            print('Not a valid JSON')
