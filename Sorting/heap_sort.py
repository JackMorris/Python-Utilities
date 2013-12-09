""" Heap Sort

Time complexity: O(nlgn)
Space complexity: O(n) total, O(1) auxiliary (in place)

"""


def _max_heapify(data, index, end_index):
    left_child_index = 2*index + 1
    right_child_index = 2*index + 2
    largest_index = index
    if left_child_index < end_index and data[left_child_index] > data[largest_index]:
        largest_index = left_child_index
    if right_child_index < end_index and data[right_child_index] > data[largest_index]:
        largest_index = right_child_index

    if largest_index != index:
        tmp = data[largest_index]
        data[largest_index] = data[index]
        data[index] = tmp
        _max_heapify(data, largest_index, end_index)


def heap_sort(data):
    # Build max heap
    heapify_start_index = int(len(data)/2)
    end_index = len(data)
    for i in range(heapify_start_index, -1, -1):
        _max_heapify(data, i, end_index)

    # Actual sort
    for i in range(end_index-1, 0, -1):
        tmp = data[0]
        data[0] = data[i]
        data[i] = tmp
        _max_heapify(data, 0, i)