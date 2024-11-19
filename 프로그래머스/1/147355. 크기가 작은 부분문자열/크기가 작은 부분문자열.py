def solution(t, p):
    answer = 0
    p_len = len(p)
    t_len = len(t)
    p=int(p)
    
    for i in range(0,t_len-p_len+1):
        if int(t[i:i+p_len]) <=p:
            answer += 1
    return answer