def solution(num_list):
    answer = 1
    answer1 = 0
    answer2 = 1
    for i in num_list:
        answer *= i
        answer1 += i
        answer2 = answer1 * answer1
        
    if answer > answer2:
            return 0
    elif answer < answer2:
            return 1
