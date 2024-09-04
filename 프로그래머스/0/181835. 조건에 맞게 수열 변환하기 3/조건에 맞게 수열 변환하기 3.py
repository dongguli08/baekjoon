def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if k % 2 == 0:
            answer.append(arr[i] + k)
        else:
            answer.append(arr[i] * k)
    return answer  # 반복문이 끝난 후에 결과를 반환
