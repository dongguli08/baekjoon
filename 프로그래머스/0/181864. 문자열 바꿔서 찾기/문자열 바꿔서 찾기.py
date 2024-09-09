def solution(myString, pat):
    answer = ''
    answer1= 0
    for i in myString:
        if i =="A":
            answer += 'B'
        elif i  =='B':
            answer += 'A'
    if pat in answer:
        answer = 1
        return answer 
    else:
        return answer1 
    

