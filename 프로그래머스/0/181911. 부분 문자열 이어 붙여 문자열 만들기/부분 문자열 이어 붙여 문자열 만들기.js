function solution(my_strings, parts) {
    let result = "";
    for(let i=0; i<my_strings.length; i++){
        const [a,b] = parts[i];
        result += my_strings[i].slice(a,b+1);
    }
    return result;
}