answer = []
N, k = map(int,input().split())

for i in range(1,N+1):
    if N % i == 0:
        answer.append(i)

answer.sort() # 이미 값은 sort되어있으므로 굳이 할 필요 없다. 

if len(answer) < k: # len(answer)를 변수로 지정해도 된다.
    result = 0  # 결과 값을 바로 print 해도 된다.
else:
    result = answer[k-1]

print(result)