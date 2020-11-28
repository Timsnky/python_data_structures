def insertion_sort(data):
    length = len(data)

    for i in range(length):
        j = i

        while j > 0 and data[j - 1] > data[j]:
            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1

data = [5, 4, 3, 2, 1]
insertion_sort(data)
print(data)
