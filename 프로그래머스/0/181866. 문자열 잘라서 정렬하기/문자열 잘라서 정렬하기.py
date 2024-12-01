def solution(myString):
    answer = myString.split('x')
    answer.sort()
    answer = list(filter(None, answer))
    return answer