def solution(my_string, s, e):
    
    answer1 = my_string[s:e+1][::-1]
    answer = my_string[:s] + answer1 + my_string[e+1:]
    return answer
