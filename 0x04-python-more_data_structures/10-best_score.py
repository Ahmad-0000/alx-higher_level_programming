#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_so_far = list(a_dictionary.keys())[0]
    for j in list(a_dictionary.keys()):
        if a_dictionary[j] > a_dictionary[best_so_far]:
            best_so_far = j
    return best_so_far
