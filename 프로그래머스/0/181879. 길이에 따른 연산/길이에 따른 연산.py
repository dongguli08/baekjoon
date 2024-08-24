def solution(num_list):
    num = len(num_list)
    
    if num >= 11:
        answer = 0
        for i in num_list:
            answer += i
    else:
        answer = 1
        for i in num_list:
            answer *= i
            
    return answer
