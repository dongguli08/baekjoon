def solution(order):
    answer = 0
       
    def switch_case(coffee):
        if coffee == "iceamericano" or coffee == "americanoice" or coffee == "hotamericano" or coffee == "americanohot" or coffee == "americano" or coffee == "anything":
            return 4500
        else:
            return 5000
            
    answer = 0
    
    for coffee in order:
        answer += switch_case(coffee)
    return answer