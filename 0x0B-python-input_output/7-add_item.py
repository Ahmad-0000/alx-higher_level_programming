#!/usr/bin/python3
"""
A script to append command line arguments to a list
in the file "add_item.json" using JSON format.
If "add_item.json" does not exist, then it will be
created.
"""
import sys
import json
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg_list = []
if len(sys.argv) > 1:
    arg_list = sys.argv[1:]

if not os.path.isfile('add_item.json'):
    with open('add_item.json', 'w') as my_file:
        pass

file_list = load_from_json_file('add_item.json')
if not file_list:
    file_list = []
save_to_json_file(file_list + arg_list, 'add_item.json')
