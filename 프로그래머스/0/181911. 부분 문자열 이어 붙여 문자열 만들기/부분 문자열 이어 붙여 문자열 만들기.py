def solution(my_strings, parts):
    answer = ''
    for string, part in zip(my_strings, parts):
        front, end = part[0], part[1]
        answer += string[front:end+1]
    return answer