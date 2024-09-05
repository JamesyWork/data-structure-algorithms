def bubble_sort(array=None):
    if array is None:
        array = [64, 34, 25, 12, 22, 11, 90, 5]

    n = len(array) - 1
    for i in range(n):
        swapped = False
        for j in range(n - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swapped = True
        if not swapped:
            break
