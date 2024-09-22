function solution(num_list) {
    let numA="",numB="";
    for(let i = 0 ; i < num_list.length ; i++){
        if(num_list[i]%2===0)
            numA+= num_list[i];
        else
            numB+= num_list[i];

    }
    return Number(numA)+ Number(numB);
}