"""
A kidnapper wrote a ransom note but is worried it will be traced back to him.
He found a magazine and wants to know if he can cut out whole words from it
and use them to create an untraceable replica of his ransom note.
The words in his note are case-sensitive and he must use whole words available
in the magazine, meaning he cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note,
print Yes if he can replicate his ransom note exactly using whole words from
the magazine; otherwise, print No.
url: https://www.hackerrank.com/challenges/ctci-ransom-note
"""

def ransom_note(magazine, ransom):
    ndict = {}
    for k in magazine:
        if k in ndict.keys():
            ndict[k] += 1
        else:
            ndict[k] = 1

    count = 0
    for item in ransom:
        if item in ndict.keys():
            value = ndict[item]
            if value > 0:
                ndict[item] -= 1
                count += 1
            else:
                break
        else:
            break
    return len(ransom) == count



def original_test():
    m, n = map(int, input().strip().split(' '))
    magazine = input().strip().split(' ')
    ransom = input().strip().split(' ')
    answer = ransom_note(magazine, ransom)
    if(answer):
        print("Yes")
    else:
        print("No")

def my_tests():

    def case0():
        quanty = "6 4"
        magazine = "give me one grand today night me Me".split(" ")
        ransom = "give one grand today".split(" ")

        return ransom_note(magazine, ransom)

    def case1():
        quanty = "6 4"
        magazine = "give me one grand today night".split(" ")
        ransom = "give one grand today at".split(" ")
        return ransom_note(magazine, ransom)

    assert case0() == True
    assert case1() == False

my_tests()


