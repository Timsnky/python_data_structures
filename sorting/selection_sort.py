def selection_sort(data):
    length = len(data)
    for i in range(length - 1):
        index = i

        for j in range(i + 1, length):
            if data[j] < data[index]:
                index = j

        if index != i:
            data[i], data[index] = data[index], data[i]


data = [5, 4, 3, 2, 1]
selection_sort(data)
print(data)
