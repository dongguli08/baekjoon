a,b,c,d= map(int,input().split())
e,f,g,h = map(int,input().split())
answer1 = a+b+c+d
answer2 = e+f+g+h
if answer1>answer2:
    print(answer1)
elif answer2>answer1:
    print(answer2)
else:
    print(answer1)