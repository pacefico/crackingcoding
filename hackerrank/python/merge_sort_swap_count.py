#!/usr/bin/python

count_swaps = 0

def merge(llist, rlist):
    global count_swaps
    """
    Merge two lists into an ordered list.
    """
    final = []
    while llist or rlist:
        # This verification is necessary for not try to compare
        # a NoneType with a valid type.
        if len(llist) and len(rlist):
            if llist[0] < rlist[0]:
                count_swaps +=1
                final.append(llist.pop(0))
            else:
                final.append(rlist.pop(0))

        # This two conditionals here, is for the case when the two lists
        # have diferent sizes. This save us of an error trying to acess
        # an index out of range.
        if not len(llist):
            if len(rlist): final.append(rlist.pop(0))

        if not len(rlist):
            if len(llist): final.append(llist.pop(0))

    return final


def merge_sort(list):
    """
    Sort the list passed by argument with merge.
    """
    if len(list) < 2: return list
    mid = int(len(list) / 2)
    return merge(merge_sort(list[:mid]), merge_sort(list[mid:]))



import random

# list = range(1, 31)
# random.shuffle(list)
# a = [2, 1, 3, 1, 2]
a = [2,4,1]
print("beg -",a)

b = merge_sort(a)

print("end -", b)

#swap_count(a, b)
print(count_swaps)