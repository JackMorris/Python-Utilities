def insertion_sort(data, min_val=0, max_val=0):
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
    return data