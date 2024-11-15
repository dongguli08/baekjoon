def solution(x):
    sum_digits = sum(int(i) for i in str(x))  # x의 각 자릿수 합
    if x % sum_digits == 0:
        return True
    else:
        return False
