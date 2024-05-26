a=int(input())
a_list=list(map(int,input().split()))
max=a_list[0]
min=a_list[0]
for i in a_list:
     if i>max:
          max=i
     elif i<min:
          min=i

print(min,max)