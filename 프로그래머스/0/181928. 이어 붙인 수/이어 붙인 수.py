def solution(num_list):
    answer1 = ''
    answer2 = ''
    
    for i in num_list:
        if i%2==0:
            answer1 += str(i)
        elif i%2!=0:
            answer2+= str(i)
    return int(answer1)+int(answer2)
