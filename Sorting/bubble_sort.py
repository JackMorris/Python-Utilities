""" Bubble Sort

Worst case time complexity: O(n^2)
Best case time complexity: O(n)
Space complexity: O(n) total, O(1) auxiliary (in place)

"""


def bubble_sort(data, min_value=0, max_value=0):
    swap_made = True
    while swap_made:
        swap_made = False
        for i in range(0, len(data)-1):
            if data[i] > data[i+1]:
                swap_made = True
                # Swap data[i] and data[i+1]
                tmp = data[i]
                data[i] = data[i+1]
                data[i+1] = tmp
    return data