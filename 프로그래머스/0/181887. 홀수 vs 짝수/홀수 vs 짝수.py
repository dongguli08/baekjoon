def solution(num_list):
    answer = 0
    answer1 = 0
    for i in range(0, len(num_list), 2):
        answer += num_list[i]
    for j in range(1, len(num_list),2):
        answer1 += num_list[j]
        
    if answer > answer1:
            return answer
    else:
            return answer1

#반복문 밖에서 비교를 해야된다
 