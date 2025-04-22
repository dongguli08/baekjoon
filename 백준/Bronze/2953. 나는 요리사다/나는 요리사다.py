
result=[0,0]

for i in range(5):
    a,b,c,d = map(int, input().split())
    sum = (a+b+c+d)
    if sum>result[1]:
        result[0] = i+1
        result[1] = sum
print(result[0])
print(result[1]) 