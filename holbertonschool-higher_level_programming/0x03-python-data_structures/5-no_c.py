#!/usr/bin/python3
def no_c(my_string):
    renovated = ""
    for i in my_string:
        if i == "c" or i == "C":
            continue
        else:
            renovated = renovated + i
    return renovated
