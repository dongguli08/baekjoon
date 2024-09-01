def solution(my_string, is_suffix):
    if my_string.endswith(is_suffix):
        return 1
    else:
        return 0
    
    #접미사 인지 확인하기