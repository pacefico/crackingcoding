
import string


def generate(n):
    import itertools
    elements = [x for x in list(string.ascii_lowercase) if x != 'y']
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [x for x in list(string.ascii_lowercase) if x != 'y' and x not in vowels]

    for subset in itertools.permutations(elements, n):
        if len(subset) >= 2:
            first = subset[0]
            result = True
            complete = first
            for i in range(len(subset)-1):
                second = subset[i+1]
                if not (first in vowels and second in consonants or second in vowels and first in consonants):
                    result = False
                    break
                complete = "{}{}".format(complete, second)
                first = second
            if result:
                print(complete)
        else:
            print("{}".format(subset[0]))

def case0():
    n = 2
    generate(n)

case0()
