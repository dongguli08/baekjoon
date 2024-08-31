def solution(num_list, n):
    # 리스트를 잘라내기
    num_list1 = num_list[:n]  # 슬라이싱이 올바르게 작동하도록 수정
    # 두 리스트를 더하기
    num_list2 = num_list[n:]
    answer = num_list2 + num_list1
    return answer