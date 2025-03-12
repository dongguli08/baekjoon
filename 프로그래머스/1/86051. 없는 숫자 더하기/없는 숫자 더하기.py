def solution(numbers):
    answer = [1,2,3,4,5,6,7,8,9,0]
    answer2 = []  
    for num in answer:
        if num not in numbers:
            answer2.append(num) 
    return sum(answer2)  
