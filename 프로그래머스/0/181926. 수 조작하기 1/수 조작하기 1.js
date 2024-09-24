
function solution(n, control) {
    var answer = n;

    for(let i of control){
        if(i == "w"){
            n += 1;
        }
        else if(i == "s"){
            n -= 1;
        }
        else if(i == "d"){
            n += 10;
        }
        else if(i == "a"){
            n -= 10;
        }
    }

    return n;
}