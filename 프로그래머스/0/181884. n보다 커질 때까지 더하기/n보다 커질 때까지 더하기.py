def solution(numbers, n):
    answer = 0  # answer를 초기화합니다.
    for i in range(len(numbers)):
        answer += numbers[i]  # 인덱스 i를 answer에 추가합니다.
        if answer > n:
            return answer
    
