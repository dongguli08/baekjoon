def solution(n):
    answer = 0
    for i in range(1, n + 1):  # 1부터 n까지 반복
        if n % i == 0:  # n이 i로 나누어 떨어지면
            answer += i  # i를 더함
    return answer
