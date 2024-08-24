def solution(arr):
    for index in range(len(arr)):
        if arr[index] >= 50 and arr[index] % 2 == 0:
            arr[index] = arr[index] // 2  # 정수 나눗셈을 위해 // 사용
        elif arr[index] <= 50 and arr[index] % 2 != 0:
            arr[index] = arr[index] * 2
    return arr
