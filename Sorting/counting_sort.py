""" Couting Sort

Time complexity: O(n)
Space complexity: O(max - min)
Min and max parameters are required as this sort is non comparative

"""


def counting_sort(data, min_value, max_value):
    count_list = [0]*(max_value-min_value+1)
    for i in range(0, len(data)):
        count_index = data[i]-min
        count_list[count_index] += 1

    count_value = max
    data_index = len(data) - 1
    while data_index >= 0:
        if count_list[count_value-min] == 0:
            count_value -= 1
        else:
            data[data_index] = count_value
            count_list[count_value-min] -= 1
            data_index -= 1