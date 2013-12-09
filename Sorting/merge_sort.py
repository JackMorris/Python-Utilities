""" Merge Sort

Time complexity: O(nlgn)
Space complexity: O(n) auxiliary

"""


def _merge(data, start_index, split_index, end_index):
    """ Merges two sorted sections of data, data[start_index:split_index] and data[split_index:end_index], placing
    the result back in data """
    tmp_result = []
    left_index = start_index
    right_index = split_index
    values_in_left = split_index - start_index
    values_in_right = end_index - split_index

    while values_in_left != 0 or values_in_right != 0:
        if values_in_left == 0 or (values_in_right != 0 and data[right_index] < data[left_index]):
            tmp_result.append(data[right_index])
            right_index += 1
            values_in_right -= 1
        else:
            tmp_result.append(data[left_index])
            left_index += 1
            values_in_left -= 1

    data[start_index:end_index] = tmp_result


def _merge_sort(data, start_index, end_index):
    """ Called by merge_sort so the sort can be done using O(n) auxiliary space """
    number_of_values = end_index-start_index
    if number_of_values <= 1:
        return
    split_index = int(number_of_values/2) + start_index
    _merge_sort(data, start_index, split_index)
    _merge_sort(data, split_index, end_index)
    _merge(data, start_index, split_index, end_index)


def merge_sort(data):
    _merge_sort(data, 0, len(data))