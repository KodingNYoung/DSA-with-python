'''
Inserts an item into a particular index in a list
works similar to python's list.insert() method
'''
def insert_item(arr, item, index):
    current_item = 0
    current_index = index
    if index >= len(arr):
        return "Enter a valid index"
    elif index == len(arr) -1:
        return "Use append function index"

    while current_index <= len(arr):
        if current_index == index:
            current_item = arr[current_index]
            arr[current_index] = item
        elif current_index == len(arr):
            arr.append(current_item)
            break
        else:
            item = current_item
            current_item = arr[current_index]
            arr[current_index] = item
        current_index += 1
    return arr

