def remove_end(arr, length):
    if length > 0:
        arr[length - 1] = 0
    
    return arr

def remove_middle(arr, i, length):
    for index in range(i + 1, length):
        arr[index - 1 ] = arr[index]

    return arr

def insert_end(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n

    return arr

def insert_middle(arr, i, n, length):
    

    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]

    arr[i] = n

    return arr

if __name__ == "__main__":

    my_array = [1, 2, 3, 4, 5]

    #output = remove_end(my_array, len(my_array))
    #output = remove_middle(my_array, 2, len(my_array))
    #output = insert_end(my_array, 6, len(my_array), 6)
    output = insert_middle(my_array, 2, 6, len(my_array))

    print(output)