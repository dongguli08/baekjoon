function solution(arr) {
    var x = [];
    for(let s of arr){
        for(let i=0;i<s;i++){
            x.push(s);
        }
    }
    return x;
}