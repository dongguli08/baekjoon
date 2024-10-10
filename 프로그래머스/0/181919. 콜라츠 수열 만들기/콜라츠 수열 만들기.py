def solution(n):
    answer = []
    answer.append(n)
    while n != 1:  # n이 1이 아닐 때까지 반복
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        answer.append(n)  # 매 반복마다 n 값을 리스트에 추가
    return answer
