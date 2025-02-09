answer = []    
for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    answer.append(a)
    
average = sum(answer) / len(answer)  
print(int(average))
