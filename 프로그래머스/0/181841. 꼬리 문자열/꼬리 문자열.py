def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex not in i:
            answer += i
    return answer 
#인덱스 번호는 필요가 없음 어짜피 결과는 문자열로 만들거임
# i 가 단어 묶음 하나씩 순환을 함 "abc"가 인덱스 1개 
#만약 abc에 ex가 포함된다면 넘어가고 포함되지 않으면 answer에 문자형태로 추가


