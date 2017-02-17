"""
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {)
occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type.
There are three types of matched pairs of brackets: [], {}, and ().
url: https://www.hackerrank.com/challenges/ctci-balanced-brackets
"""

import re


def is_matched(expression):
    open_brackets = ["[", "{", "("]
    close_brackets = ["]", "}", ")"]
    stack = []
    for item in expression:
        if item in open_brackets:
            stack.append(item)
        else:
            if len(stack) == 0 or stack.pop() != open_brackets[close_brackets.index(item)]:
                return False
    return True if len(stack) == 0 else False

def original_tests():
    t = int(input().strip())
    for a0 in range(t):
        expression = input().strip()
        if is_matched(expression) == True:
            print("YES")
        else:
            print("NO")

def my_tests():
    def case0():
        return "{[()]}"

    def case1():
        return "{[(])}"

    def case2():
        return "{{[[(())]]}}"

    def case3():
        return "{{[[(())]]}}["

    assert is_matched(case0()) == True
    assert is_matched(case1()) == False
    assert is_matched(case2()) == True
    assert is_matched(case3()) == False

my_tests()