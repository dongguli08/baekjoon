def solution(my_string, s, e):
    # s부터 e까지의 부분 문자열을 반전
    answer1 = my_string[s:e+1][::-1]
    # s 이전 부분, 반전된 부분 문자열, e 이후 부분을 연결
    answer = my_string[:s] + answer1 + my_string[e+1:]
    return answer
