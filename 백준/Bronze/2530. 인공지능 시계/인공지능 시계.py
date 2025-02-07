a, b, c = map(int, input().split())  # 현재 시, 분, 초 입력
d = int(input())  # 추가할 초 입력

# d를 시, 분, 초로 변환
hours = d // 3600  
minutes = (d % 3600) // 60  
seconds = d % 60  

# 현재 시간에 더하기
answer1 = a + hours  
answer2 = b + minutes  
answer3 = c + seconds  

# 초가 60 이상이면 분 증가
if answer3 >= 60:
    answer2 += 1
    answer3 -= 60

# 분이 60 이상이면 시간 증가
if answer2 >= 60:
    answer1 += 1
    answer2 -= 60

# 24시간제 적용
answer1 %= 24  

print(answer1, answer2, answer3)
