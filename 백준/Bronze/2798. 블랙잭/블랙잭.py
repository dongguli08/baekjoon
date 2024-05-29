from itertools import combinations

a,b=map(int,input().split())
c=list(map(int,input().split()))
biggest_sum=0


for i in combinations(c,3):
        list_sum=sum(i)
        if biggest_sum<list_sum<=b:
         biggest_sum=list_sum
print(biggest_sum)
