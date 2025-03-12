def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if not answer:  #is none은 아무것도 없어야함 어떠한것도
        answer = [-1]
    else:
        answer.sort()
    return answer
