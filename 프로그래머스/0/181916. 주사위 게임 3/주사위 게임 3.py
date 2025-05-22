def solution(a, b, c, d):
    x = [a, b, c, d]
    x.sort()   # 주사위 리스트 오름차순 정렬
 
    # 1. 네 주사위가 모두 같을 경우
    if x[0] == x[3] :  
        return 1111*a
 
    # 2. 세 주사위가 같을 경우
    elif x[0] == x[2] : 
        return (10 * x[1] + x[3])**2
    elif x[1] == x[3] : 
        return (10 * x[1] + x[0])**2
    
    # 3. 두 개씩 같을 경우
    elif x[0] == x[1] and x[2] == x[3] :
        return (x[0] + x[3]) * abs(x[0] - x[3])
    
    # 4. 두 개만 같고, 나머지는 각각 다를 경우
    elif x[0] == x[1] : 
        return x[2] * x[3]
    elif x[1] == x[2] : 
        return x[0] * x[3]
    elif x[2] == x[3] : 
        return x[0] * x[1]
    
    # 5. 네 주사위가 모두 다를 경우
    else :
        return x[0]