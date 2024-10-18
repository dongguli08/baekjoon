function solution(num_list) {
    var answer = [];
    num_list.sort(function(a, b) { return a - b; });
    return num_list.slice(5);
}
