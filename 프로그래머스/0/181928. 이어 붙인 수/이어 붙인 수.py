def solution(num_list):
    answer = ''
    answer1 = ''
    for num in num_list:
        if num % 2 != 0:
            answer += str(num)
        if num%2==0:
            answer1 +=str(num) 
    return int(answer)+int(answer1)
