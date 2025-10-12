def solution(arr):
    answer = []
    
    row = len(arr)
    col = len(arr[0])
    
    if row > col:
        for i in arr:
            answer.append(i + [0] * (row - col))
    elif row < col:
        for _ in range(col - row):
            arr.append([0] * col)
        answer = arr
    else:
        answer = arr
    
    return answer