def solution(numbers, target):
    answer = 0
    
    def dfs(index, sum):
        nonlocal answer
        
        # 1️⃣ 모든 숫자를 다 사용했는지 확인
        if index == len(numbers):
            if sum == target:
                answer += 1
            return
        
        # 2️⃣ + 선택
        dfs(index + 1, sum + numbers[index])
        
        # 3️⃣ - 선택
        dfs(index + 1, sum - numbers[index])
    
    dfs(0, 0)
    
    return answer