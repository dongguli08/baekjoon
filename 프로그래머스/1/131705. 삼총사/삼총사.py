from itertools import combinations

def solution(number):
    answer = 0
    for nums in combinations(number,3):
        if sum(nums) == 0:
            answer+=1
    return answer
