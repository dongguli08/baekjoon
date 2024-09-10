def solution(arr1, arr2):
    answer = 0
    answer1 = 0
    answer2 = 0
    if len(arr1)>len(arr2):
        answer = 1
    elif len(arr1)<len(arr2):
        answer = -1
    elif len(arr1) == len(arr2):
        for i in arr1:
            answer1+=i
        for j in arr2:
            answer2+=j
            if answer1>answer2:
                answer = 1
            elif answer1<answer2:
                answer = -1
            else:
                answer = 0
    return answer