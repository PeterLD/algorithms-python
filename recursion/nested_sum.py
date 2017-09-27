# Write a function that sums all numbers in an array that can have nested sub-arrays. Do not use loops.

def nested_sum(arr):
    arr_sum = 0

    for item in arr:
        if isinstance(item, int):
            arr_sum += item
        elif isinstance(item, list):
            arr_sum += nested_sum(item)

    return arr_sum
