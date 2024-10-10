# def solution(arr, idx):
#     for i in range(idx, len(arr)):
#         if arr[i] == 1:
#             return i
#     return -1

def solution(arr, idx):
    answer = -1  # 기본값 -1
    for i in range(len(arr)):  # 배열 전체 순회
        if arr[i] == 1 and i >= idx:  # 1을 찾고 i가 idx보다 크거나 같으면
            answer = i
            break  # 첫 번째 1을 찾으면 반복문 종료
    return answer
