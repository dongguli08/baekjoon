def solution(ineq, eq, n, m):
    if eq == "!" :
        if ineq == "<" :
             return int(n<m) #리턴의 조건 값이 만족하면 1반환
        else:
            return int(n>m) #만족 못하면 0반환
    else:
        if ineq == "<" :
             return int(n<=m)
        else:
            return int(n>=m)