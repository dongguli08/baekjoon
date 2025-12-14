import string

def solution(s, skip, index):
    alphabet = string.ascii_lowercase
    skip_set = set(skip)      # 포함 여부 O(1)
    answer = ''

    for ch in s:
        cur = alphabet.index(ch)
        moved = 0

        while moved < index:
            cur = (cur + 1) % 26   # z 넘어가면 a로 순환

            if alphabet[cur] in skip_set:
                continue          # skip이면 카운트 안 함

            moved += 1

        answer += alphabet[cur]

    return answer
