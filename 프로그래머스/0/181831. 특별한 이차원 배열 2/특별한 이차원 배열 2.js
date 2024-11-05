function solution(arr) {
    var answer = 0;
    for(let i=0;i<arr.length;i++){
        for(let j=0;j<arr.length;j++){
            if(arr[i][j]!==arr[j][i]) {

               return answer=0
            }
            else {answer=1}
        }
    }
    return answer;
}

console.log(solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))
console.log(solution([[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723],
 [587, 754, 723, 81]]))