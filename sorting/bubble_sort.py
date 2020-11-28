def bubble_sort(data):
    length = len(data)

    for i in range(length - 1):
        for j in range(length - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


data = [5, 4, 3, 2, 1]
bubble_sort(data)

print(data)
