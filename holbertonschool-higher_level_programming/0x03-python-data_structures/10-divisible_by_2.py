#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for pos in my_list:
        if pos % 2 is 0:
            new_list += [True]
        else:
            new_list += [False]
    print(new_list)
    for e in new_list:
        print(type(e))
    return new_list
