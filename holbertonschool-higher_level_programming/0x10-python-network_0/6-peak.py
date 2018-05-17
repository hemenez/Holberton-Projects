#!/usr/bin/python3
def find_peak(list_of_integers):
    """ Fxn finds peak in list of integers """
    if list_of_integers is not None:
        before = 0
        current = 1
        after = 2
        num = list_of_integers
        while after != len(list_of_integers):
            if num[before] < num[current] > num[after]:
                return num[current]
            before += 1
            current += 1
            after += 1
#        for idx in range(1, len(num)):
#            if num[idx - 1] < num[idx] > num[idx + 1]:
#                return num[idx]
