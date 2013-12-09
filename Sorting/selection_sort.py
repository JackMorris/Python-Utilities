def selection_sort(data, min_val=0, max_val=0):
    for i in range(0, len(data)):
        current_min_index = i
        for j in range(i+1, len(data)):
            if data[j] < data[current_min_index]:
                current_min_index = j

        # Swap data[i] and data[current_min_index]
        tmp = data[i]
        data[i] = data[current_min_index]
        data[current_min_index] = tmp
    return data