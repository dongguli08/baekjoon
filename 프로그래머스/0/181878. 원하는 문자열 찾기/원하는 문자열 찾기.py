def solution(myString, pat):
    answer = 0
    myString2 = myString.upper()
    pat2 = pat.upper()
    if pat2 in myString2:
        answer = 1
    else:
        answer = 0
    return answer