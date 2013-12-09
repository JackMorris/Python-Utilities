""" Insertion Sort

Worst case time complexity: O(n^2)
Best case time complexity: O(n)
Space complexity: O(n) total, O(1) auxiliary (in place)

"""


def insertion_sort(data):
    for i in range(1, len(data)):
        # data[0:i] already sorted
        to_insert = data[i]
        j = i
        while j > 0:
            if to_insert < data[j-1]:
                data[j] = data[j-1]
                j -= 1
            else:
                break
        data[j] = to_insert