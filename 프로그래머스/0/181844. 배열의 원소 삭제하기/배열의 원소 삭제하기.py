def solution(arr, delete_list):
    i = 0
    while i < len(arr):
        if arr[i] in delete_list:
            arr.pop(i)
        else:
            i += 1
    return arr
