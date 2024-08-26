def solution(a, b):
    answer1 = int(str(a) + str(b))  # a와 b를 문자열로 변환하여 이어붙인 후 정수로 변환
    answer2 = int(str(b) + str(a))  # b와 a를 문자열로 변환하여 이어붙인 후 정수로 변환
    
    # 두 값 중 더 큰 값을 반환
    return max(answer1, answer2)
