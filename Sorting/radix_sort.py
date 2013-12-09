""" Radix Sort

Time complexity: O(kn) (k = digits_in_max)
Space complexity: O(n)
Note: only valid when all values in data > 0

"""


def radix_sort(data):
    if len(data) <= 1:
        return
    max_value = max(data)
    digits_in_max = len(str(max_value))
    for i in range(0, digits_in_max):
        bins = []
        for j in range(0, 10):
            bins.append([])
        div_power = 10**i
        for v in data:
            sort_digit = int(v/div_power) % 10
            bins[sort_digit].append(v)
        data_index = 0
        for b in bins:
            for v in b:
                data[data_index] = v
                data_index += 1