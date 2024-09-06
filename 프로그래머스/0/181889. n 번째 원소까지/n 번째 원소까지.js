function solution(num_list, n) {
    let answer = [];
    for(let i=0; i<n; i++){
        answer.push(num_list[i]);
        if (i>n){
        break;
        }
        }
    return answer
    }
        