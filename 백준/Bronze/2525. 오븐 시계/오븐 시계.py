
a,b=map(int,input().split())
c=int(input())

if b+c<60:
    print(a,b+c)

else:
    hour=(b+c)//60
    min=(b+c)%60

    if(a+hour<24):
        print(a+hour,min)
    else:
        print(a+hour-24,min)