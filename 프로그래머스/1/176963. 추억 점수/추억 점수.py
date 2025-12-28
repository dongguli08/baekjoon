def solution(name, yearning, photo):
    # 1. 이름과 점수를 매핑
    score_dict = {}
    for i in range(len(name)):
        score_dict[name[i]] = yearning[i]
    
    answer = []
    
    # 2. 각 사진별 점수 계산
    for p in photo:
        total = 0
        for person in p:
            if person in score_dict:
                total += score_dict[person]
        answer.append(total)
    
    return answer
