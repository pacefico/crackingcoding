
"""
string_common_divisor.py

for each number from 1 to N+1 print if it is divided by elements in a list
if true for more than one, print on the given order else print only the number

"""

my_list = [
    (3, "Fizz"),
    (5, "Buzz"),
    (7, "Woof")
]

def solution(N):
    for i in range(1, N+1):
        my_str = ""
        for j in my_list:
            if i % j[0] == 0:
                my_str += j[1]

        if len(my_str) == 0:
            print(i)
        else:
            print(my_str)

solution(100)
