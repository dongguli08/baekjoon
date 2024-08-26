#def solution(n):
    #answer = 0
    #if n % 2 == 0:
       # for i in range(n):  #이 코드는 n 자기 자신을 포함하지 않음
      #      if(i%2==0):
     #           answer += i * i
    #else:
        #for i in range(n):
            #if(i%2!=0):
               # answer += i
    #return answer

def solution(n):
    answer = 0
    if n % 2 == 0:
        # n이 짝수일 때, n 이하의 짝수의 제곱의 합
        for i in range(2, n + 1, 2):  # 2부터 n까지 짝수만 선택
            answer += i * i
    else:
        # n이 홀수일 때, n 이하의 홀수의 합
        for i in range(1, n + 1, 2):  # 1부터 n까지 홀수만 선택
            answer += i
    return answer
