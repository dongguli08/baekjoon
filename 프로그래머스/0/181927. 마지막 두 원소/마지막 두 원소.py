def solution(num_list):
    a = num_list[-1]
    b = num_list[-2]
    c = 0
    
    if a > b:
        c = a - b
        return num_list + [c]
    else:
        c = a * 2
        
        return num_list + [c]
#list(c)에서 c가 정수형이면 TypeError가 발생합니다. 이는 list 함수가 반복 가능한 객체만을 인자로 받아야 하기 때문입니다. 
# 즉 반복 가능한 객체는 튜플,문자열 등