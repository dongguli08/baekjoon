def solution(str1, str2):
    answer = 0
    for i in str2:
        if str1 in str2:
            answer = 1
        else:
            answer = 0
    return answer