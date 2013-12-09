""" Counting Sort

Time complexity: O(n)
Space complexity: O(max_value - min_value)

"""


def counting_sort(data):
    min_value = min(data)
    max_value = max(data)
    count_list = [0]*(max_value-min_value+1)
    for i in range(0, len(data)):
        count_index = data[i]-min_value
        count_list[count_index] += 1

    count_value = max_value
    data_index = len(data) - 1
    while data_index >= 0:
        if count_list[count_value-min_value] == 0:
            count_value -= 1
        else:
            data[data_index] = count_value
            count_list[count_value-min_value] -= 1
            data_index -= 1