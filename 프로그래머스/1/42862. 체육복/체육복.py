def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    lost_set = set(lost)
    reserve_set = set(reserve)

    # lost와 reserve 중복 제거 (자기 자신만 해결하는 경우)
    overlap = lost_set & reserve_set
    lost_set -= overlap
    reserve_set -= overlap

    # 빌려주는 처리
    for r in reserve_set:
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)

    answer = n - len(lost_set)
    return answer
