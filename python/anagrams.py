"""
Alice is taking a cryptography class and finding anagrams to be very useful.
We consider two strings to be anagrams of each other if the first string's letters
can be rearranged to form the second string. In other words, both strings must
contain the same exact letters in the same exact frequency
For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption
is dependent on the minimum number of character deletions required to make the two
strings anagrams. Can you help her find this number?

Given two strings,  and , that may or may not be of the same length, determine the
minimum number of character deletions required to make  and  anagrams. Any characters
can be deleted from either of the strings.
url: https://www.hackerrank.com/challenges/ctci-making-anagrams
"""


def number_needed(a,b):
    """
        counts the 'minimum' amount of character that needs to be removed from 2 strings
        in order to get them anagrams of each other
    :param a: first string to be counted
    :param b: second string to be counted
    :return: total amount of strings that need to be removed
    """
    count = 0
    for x in set(a):
        count += min(a.count(x), b.count(x))

    return len(a) + len(b) - 2*count

def case0():
    a = "abc"
    b = "cde"
    return number_needed(a, b)

def case1():
    a = "gwoydkkstkgaluglmwusqlpgozlvocxskfrrfhlowwzybguzps"
    b = "qlkwlpwhbtuefedscyeualrzfdnzks"
    return number_needed(a, b)

def case2():
    a="afaaa"
    b="afff"
    return number_needed(a, b)

def case3():
    a="afaaa"
    b="afff"
    return number_needed(a, b)

def case4():
    a="bacdc"
    b="dcbac"
    return number_needed(a, b)

def case5():
    a="bacdc"
    b="dcbad"
    return number_needed(a, b)

assert case0() == 4
assert case1() == 30
assert case2() == 5
assert case4() == 0
assert case5() == 2

