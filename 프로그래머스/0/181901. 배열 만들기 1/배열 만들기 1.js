function solution(n, k) {
    var answer = [];
    for(var i = k; i <= n; i+=k){
        answer.push(i);
    }
    return answer;
}