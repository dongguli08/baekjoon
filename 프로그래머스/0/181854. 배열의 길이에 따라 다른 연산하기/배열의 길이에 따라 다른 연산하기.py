def solution(arr, n):
    answer = []
    length = len(arr)
    
    if length%2==0:
        for i in range(len(arr)):
            if i%2!=0:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])    
    
    elif length%2!=0:
        for i in range(len(arr)):
            if i%2==0:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
        
    return answer