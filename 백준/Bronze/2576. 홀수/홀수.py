answer = 0
number = float('inf')  # 가장 큰 수로 초기화 (입력되는 숫자 중 가장 작은 값을 찾기 위함)
has_odd = False  # 홀수가 있는지 확인할 변수

# 7개의 숫자를 입력받음
for i in range(7):
    num = int(input())  # 숫자를 입력받음
    if num % 2 != 0:  # 홀수일 때만
        has_odd = True  # 홀수가 있다는 플래그 설정
        answer += num  # 홀수를 answer에 더함
        if num < number:  # num이 현재 number보다 작으면
            number = num  # number 값을 num으로 변경

# 홀수가 없을 경우 -1 출력
if not has_odd:
    print(-1)
else:
    print(answer)
    print(number)
