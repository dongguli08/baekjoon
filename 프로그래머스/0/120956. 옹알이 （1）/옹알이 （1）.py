def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    answer = len(babbling)
    dict = {}
    for b in babbling:
        if b not in dict:
            dict[b] = 0
        for c in can:
            if b.find(c)>-1:
                dict[b] += 1
    for b in range(len(babbling)):
        for i in range(dict[babbling[b]]):
            for c in can:
                babbling[b] = babbling[b].split(c)[1] if babbling[b].startswith(c) else babbling[b]
    
    return len([i for i in babbling if len(i) == 0])