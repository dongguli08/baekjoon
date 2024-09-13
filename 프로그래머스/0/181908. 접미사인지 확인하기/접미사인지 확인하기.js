// function solution(my_string, is_suffix) {
//     var answer = 0;
//     if (my_string.endsWith(is_suffix)){
//         answer = 1
//     }
//     else{
//         answer = 0
//     }
//     return answer;
// }
function solution(my_string, is_suffix) {
    var answer = 0;

    for (let i = 0; i <= my_string.length - is_suffix.length; i++) {
        if (my_string.slice(i) === is_suffix) {
            return 1;
        }
    }

    return answer;
}
