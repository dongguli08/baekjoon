a,b=map(int,input().split())
a_list=list(map(int,input().split()))

for i in range(a):
    if a_list[i]<b:
        print(a_list[i],end=" ")