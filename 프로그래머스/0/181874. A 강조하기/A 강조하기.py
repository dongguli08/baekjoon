def solution(myString):
    answer = ''
    for i in myString:
        if i.lower()!= 'a':
            answer +=i.lower()
        else:
            answer += 'A'
    return answer