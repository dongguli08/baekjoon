N = int(input())
customer = list(map(int, input().split()))
sit = [0 for j in range(101)]
cnt = 0
for i in customer:
    if sit[i] == 0:
        sit[i] = i
    else:
        cnt += 1
print(cnt)