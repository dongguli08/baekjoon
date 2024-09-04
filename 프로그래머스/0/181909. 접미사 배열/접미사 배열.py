def solution(my_string):
    # 모든 접미사를 구하는 리스트 생성
    suffixes = [my_string[i:] for i in range(len(my_string))]
    
    # 접미사를 사전순으로 정렬
    suffixes.sort()
    
    # 정렬된 접미사 리스트 반환
    return suffixes
