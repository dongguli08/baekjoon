import sys
input = sys.stdin.readline

for i in range(3):  
    n = int(input())  # 이 케이스에서 입력될 숫자 개수
    total = 0
    for i in range(n):
        total += int(input())
    if total > 0:
        print('+')
    elif total < 0:
        print('-')
    else:
        print('0')
