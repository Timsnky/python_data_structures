def merge_sort(data):
    length = len(data)

    if length == 1:
        return

    middle_index = length // 2

    lower_half = data[: middle_index]
    upper_half = data[middle_index:]

    merge_sort(lower_half)
    merge_sort(upper_half)

    i = j = k = 0

    while i < len(lower_half) and j < len(upper_half):
        if lower_half[i] < upper_half[j]:
            data[k] = lower_half[i]
            i += 1
        else:
            data[k] = upper_half[j]
            j += 1
        k += 1

    while i < len(lower_half):
        data[k] = lower_half[i]
        k += 1
        i += 1

    while j < len(upper_half):
        data[k] = upper_half[j]
        k += 1
        j += 1


data = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]
merge_sort(data)
print(data)
