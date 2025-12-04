
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
def solution(schedules, timelogs, startday):
    result = 0

    # 직원 순회
    for i in range(len(schedules)):
        schedule = convert(schedules[i]) + 10
        timelog = timelogs[i]
        cur_day = startday - 1

        # 출근 기록 순회
        for log in timelog:
            cur_day += 1

            # 토, 일은 제외
            if cur_day % 7 in [0, 6]:
                continue

            # 지각 체크
            if convert(log) > schedule:
                break
        else:
            result += 1

    return result

def convert(time):
    time = str(time)
    h, m = time[:-2], time[-2:]
    return int(h)*60 + int(m)