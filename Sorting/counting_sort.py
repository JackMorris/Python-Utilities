""" Counting Sort

Time complexity: O(n)
Space complexity: O(max_value - min_value)

"""


def counting_sort(data):
    if len(data) <= 1:
        return
    min_value = min(data)
    max_value = max(data)
    count_list = [0]*(max_value-min_value+1)
    for i in range(0, len(data)):
        count_index = data[i]-min_value
        count_list[count_index] += 1

    # Traverse both data and count_list, updating values in data as appropriate
    count_index = 0
    for i in range(0, len(data)):
        while count_list[count_index] == 0:
            count_index += 1
        data[i] = count_index + min_value
        count_list[count_index] -= 1