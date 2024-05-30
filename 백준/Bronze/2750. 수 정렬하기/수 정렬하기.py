n = int(input())
a = []
for _ in range(n):
    number = int(input())
    a.append(number)
a.sort()
for number in a:
    print(number)
