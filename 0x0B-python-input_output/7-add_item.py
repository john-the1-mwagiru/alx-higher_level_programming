#!/usr/bin/python3
"""This module adds all arguments to a Python list, and then save them to a file"""

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_all_arguments(my_obj, filename="add_item.json"):
    save_to_json_file(my_obj, filename="add_item.json")
    load_from_json_file(filename="add_item.json")
