def solution(number):
    answer = 0
    answer1 =0
    for i in number:
        answer += int(i)
    answer1 = answer %9
    return answer1