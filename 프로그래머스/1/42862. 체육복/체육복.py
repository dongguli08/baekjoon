def solution(n, lost, reserve):
    answer = 0
    # 1.set으로 자료형을 바꾸고
    # 2.lost와 reserve에 같은 값이 있으면 둘 다에서 삭제
    # 3.for 문을 돌면서 r-1 값이 lost에 있는지
    # 4. r+1값이 lost에 있는지 확인
    # 5. n에서 lost의 길이 만큼 빼기
    
    lost.sort()
    reserve.sort()
    
    #set 으로 바꾸는 방법 알기 (list->set은 중복제거와,인덱스로 접근 불가)
    reserve_set = set(reserve)
    lost_set = set(lost)

    both = reserve_set & lost_set
    reserve_set -=both
    lost_set -= both
    
    for r in reserve_set:
        if r-1 in lost_set:
            lost_set.remove(r-1) # lost_set에서 r-1 값 삭제
        elif r+1 in lost_set:
            lost_set.remove(r+1)
            
    answer = n-len(lost_set)
    
    return answer