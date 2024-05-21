#!/usr/bin/python3
"""A script that takes a letter as a paremeter, sends it to 
"http://0.0.0.0:5000/search_user" and handles JSON response bodies"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = {'q': ""}
    if len(sys.argv) > 1:
        letter['q'] = sys.argv[1]
    response = requests.post(url, data=letter)
    try:
        json_dict = response.json()
        print(f'[{json_dict["id"]}] {json_dict["name"]}')
    except Exception:
        if not response.text:
            print('No result')
        else:
            print('Not a valid JSON')
