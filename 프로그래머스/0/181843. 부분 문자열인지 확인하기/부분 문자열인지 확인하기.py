def solution(my_string, target):
    answer = 0
    for i in my_string:
        if target in my_string:
            answer=1
    return answer