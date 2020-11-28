def swap(data, index1, index2):
    data[index1], data[index2] = data[index2], data[index1]


def partition(data, low, high):
    pivot = (low + high) // 2
    swap(data, pivot, high)

    i = low

    for j in range(low, high):
        if data[j] <= data[high]:
            swap(data, j, i)
            i += 1

    swap(data, i, high)

    return i


def quick_sort(data, low, high):
    if low >= high:
        return

    pivot_index = partition(data, low, high)
    quick_sort(data, low, pivot_index - 1)
    quick_sort(data, pivot_index + 1, high)


data = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]
quick_sort(data, 0, len(data) - 1)
print(data)