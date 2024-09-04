def solution(a, d, included):
    total_sum = 0
    for i in range(len(included)):
        if included[i]:  # included[i]가 True일 때
            term = a + i * d  # i번째 항 계산
            total_sum += term  # 더하기
    return total_sum
