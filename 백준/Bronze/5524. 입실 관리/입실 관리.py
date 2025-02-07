a = int(input())
words = []
for i in range(a):
    word = input("").lower()  # 소문자로 변환
    words.append(word)

# 단어를 줄바꿈하며 출력
for word in words:
    print(word)
