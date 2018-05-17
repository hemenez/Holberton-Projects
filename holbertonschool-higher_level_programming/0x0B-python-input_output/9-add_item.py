#!/usr/bin/python3
import sys
import json
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"

with open(filename, "a+", encoding="utf-8") as my_file:
    obj_1 = load_from_json_file(filename)
#    my_list = []
    index = 0
    for i in sys.argv:
        if sys.argv[index] == 0:
            pass
        else:
            obj_1.append(sys.argv[index])
        index = index + 1
    save_to_json_file(obj_1, my_file)
