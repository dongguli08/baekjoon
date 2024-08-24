def solution(my_string, overwrite_string, s):
    # 첫 번째 부분: 덮어쓰기 시작 전의 부분
    first_part = my_string[:s]
    
    # 세 번째 부분: 덮어쓰기가 끝난 후의 나머지 부분
    third_part = my_string[s + len(overwrite_string):]
    
    # 결과 문자열
    result = first_part + overwrite_string + third_part
    
    return result

