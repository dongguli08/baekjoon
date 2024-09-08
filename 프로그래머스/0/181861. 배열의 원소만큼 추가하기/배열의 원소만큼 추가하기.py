def solution(arr):
    answer = []
    for i in arr:
        for _ in range(i):  # i의 값만큼 반복
            answer.append(i)  # i를 추가
    return answer
