def solution(num_list, n):
    answer = 0
    for i in num_list:
        if n in num_list:
            answer = 1
    return answer