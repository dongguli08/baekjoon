N = input()
M = input()
 
num = int(N[:-2]) * (100)
while (True) :
    if num % int(M) == 0 :
        break
    num += 1

print(str(num)[-2:])