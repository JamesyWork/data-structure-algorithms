def find_lowest_value(array=None):
    if array is None:
        array = [7, 12, 9, 4, 11]

    min_value = array[0]
    for value in array:
        print(value, min_value)
        if value < min_value:
            min_value = value

    print(min_value)
