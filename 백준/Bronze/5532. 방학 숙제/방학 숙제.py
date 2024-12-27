import math

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

answer1 = math.ceil(a/c)
answer2 = math.ceil(b/d)
answer3 = 0
if answer1>=answer2:
    answer3=l-answer1
elif answer2>=answer1:
    answer3 = l-answer2

print(answer3)