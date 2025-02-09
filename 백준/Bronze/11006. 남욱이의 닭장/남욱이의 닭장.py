T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    N, M = map(int, input().split())  # 다리 합 N, 닭 수 M 입력
    
    U = 2 * M - N  # 다리가 잘린 닭 수
    T = M - U  # 멀쩡한 닭 수

    print(U, T)  # 결과 출력