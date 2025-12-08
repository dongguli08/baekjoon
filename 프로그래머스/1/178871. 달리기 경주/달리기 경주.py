def solution(players, callings):
    # 선수 이름 -> 현재 인덱스
    pos = {player: i for i, player in enumerate(players)}
    
    for name in callings:
        idx = pos[name]
        if idx > 0:
            # 앞 선수와 교환
            players[idx], players[idx-1] = players[idx-1], players[idx]
            
            # 위치 정보 업데이트
            pos[players[idx]] = idx
            pos[players[idx-1]] = idx-1
    
    return players