""" Quicksort

Time complexity: O(n^2)
Space complexity: O(n) total, O(1) auxiliary (in place)

"""


def _partition(data, start_index, end_index):
    """ Partitions data into two sections, less than partition value and greater than partition value. Partition
    value chosen as last element in data. Partition value moved between sections in data, and its index returned.
    """
    partition_value = data[end_index-1]
    i = start_index - 1
    for j in range(start_index, end_index-1):
        if data[j] <= partition_value:
            i += 1
            tmp = data[i]
            data[i] = data[j]
            data[j] = tmp
    tmp = data[i+1]
    data[i+1] = data[end_index-1]
    data[end_index-1] = tmp
    return i+1


def _quicksort(data, start_index, end_index):
    """ Called by quicksort() so the sort can be done recursively in place """
    if start_index >= end_index:
        return
    partition_index = _partition(data, start_index, end_index)
    _quicksort(data, start_index, partition_index)
    _quicksort(data, partition_index+1, end_index)


def quicksort(data):
    _quicksort(data, 0, len(data))