#!/bin/python3
"""
Solution for https://www.hackerrank.com/challenges/two-characters/problem
"""
import math
import os
import random
import re
import sys


def show(obj):
    # print(obj)
    pass
# Complete the alternate function below.


def getUniqeChar(s):
    return set(s)

"""
Get Unique pair of combination index for a specific length of list
if lenghth = 4 [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
if lenghth = 3 [(0, 1), (0, 2)]
if lenghth = 2 [(0, 1)]
"""
def getUniquePairIndex(lenght):
    if lenght < 2:
        raise Exception("Invalid length; must be >=2")
    unique_pair_index_list = []
    index = 0
    while index <= lenght - 1:
        index_j = index + 1
        while index_j <= lenght - 1:
            unique_pair_index_list.append((index, index_j))
            index_j = index_j + 1
        index = index + 1
    return unique_pair_index_list
    # return [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

"""
Get Unique pair of combination charecter touple
for a list of unique char list [a,b,e,f] unique pair will be [('a', 'b'), ('a', 'e'), ('a', 'f'), ('b', 'e'), ('b', 'f'), ('e', 'f')]
"""
def getUniquePair(unique_char_list):
    lenght = len(unique_char_list)
    if lenght < 2:
        raise Exception("No of unique charecters are less than 2")
    unique_pair_list = []
    if lenght == 2:
        unique_pair_list = [(unique_char_list[0], unique_char_list[1])]
    else:
        unique_pair_index_list = getUniquePairIndex(lenght)
        show("Unique Pair Index List {}".format(unique_pair_index_list))
        for each_unique_pair_index in unique_pair_index_list:
            unique_pair_list.append((
                unique_char_list[each_unique_pair_index[0]], unique_char_list[each_unique_pair_index[1]]))
    return unique_pair_list
"""
whether a string has only given pair as alternate charecters
"""
def isAlternate(s,pair):
    char_seen = ''
    for element in s:
        if element in pair:
            if (char_seen != element):
                char_seen = element
            else:
                return False
        else:
            return False
    return True
"""
Remove all charecter from string except given pair
"""
def removeAllExceptPair(s, each_pair):
    for element in s:
        if element not in each_pair:
            s = s.replace(element, '')
    show("After removing - {}".format(s))
    return s
"""
get the longest string out of a given list
"""
def getLongestAlternate(alternate_list):
    longest_alternate = ''
    for each_alternate_str in alternate_list:
        if len(each_alternate_str) > len(longest_alternate):
            longest_alternate = each_alternate_str
    show(longest_alternate)
    return longest_alternate

"""
1. Find set of uqnique characters
2. Find unique pair of characters out of uqnique characters set
3. For each pair remove all characters except that pair and save value to a temp string
4. Verify temp string is following alternate sequence
5. If following alternate sequence then add to a list and find more possible alternate string (step 3-4)
6. Out of all possible alternate string find the longest one

"""
def alternate(s):
    try:
        alternate_list = []
        unique_char_list = list(getUniqeChar(s))
        show(unique_char_list)
        unique_pair_list = getUniquePair(unique_char_list)
        show("Unique Pair List {}".format(unique_pair_list))
        for each_pair in unique_pair_list:
            # show(each_pair)
            temp_str = removeAllExceptPair(s, each_pair)
            # show(temp_str)
            if(isAlternate(temp_str,each_pair)):
                show("alternate found-{}".format(temp_str))
                alternate_list.append(temp_str)
        return len(getLongestAlternate(alternate_list))
    except:
        return 0
def call(s):
    result = alternate(s)
    print(result)
call('beabeefeab')
call('asdcbsdcagfsdbgdfanfghbsfdab')
call('asvkugfiugsalddlasguifgukvsa')
call('ab')
call('a')
call('')
call('abc')
