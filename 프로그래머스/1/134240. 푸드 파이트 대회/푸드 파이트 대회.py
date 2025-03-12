def solution(food):
    answer = ''
    answer1 = ''
    for i in range(1, len(food)):
        number = food[i] // 2
        for j in range(number):
            answer += str(i)
    answer1 = ''.join(reversed(answer))
    return answer + '0' + answer1


