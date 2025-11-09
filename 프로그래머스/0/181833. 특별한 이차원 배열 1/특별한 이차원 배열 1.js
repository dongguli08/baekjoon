function solution(n) {
    // 각 행을 나타내는 배열 생성
    let arr = []; 
    for(let i=0; i<n; i++){
        let row = [];
        for(let j=0; j<n; j++){
            row.push(i===j ? 1 : 0)
        }
         // 전체 배열에 행을 추가
        arr.push(row);
    }
    return arr;
}