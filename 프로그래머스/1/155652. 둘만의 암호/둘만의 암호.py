import string

def solution(s, skip, index):
    alphabet = string.ascii_lowercase
    skip_set = set(skip)      # 포함 여부 O(1)
    answer = ''

    for i in s:
        location = alphabet.index(i) #현재 알파벳 인덱스 위치
        number = 0
        
        while number < index:
            location = (location+1)%26
        
            if alphabet[location] in skip_set: 
                continue
                
            number +=1
        
        answer+=alphabet[location] #현재 인덱스의 알파벳
        
    return answer
