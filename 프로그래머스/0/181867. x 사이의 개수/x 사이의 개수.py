def solution(myString):
    tmp = myString.split("x")
    return [len(i) for i in tmp]
