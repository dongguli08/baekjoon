def solution(start, end):
    answer = []  # 빈 리스트로 초기화
    for i in range(start, end + 1):
        answer.append(i)  # 리스트에 i 추가
    return answer  # 루프가 끝난 후 리스트 반환
