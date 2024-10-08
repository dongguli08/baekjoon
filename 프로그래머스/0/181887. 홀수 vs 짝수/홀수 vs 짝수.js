function solution(num_list) {
    let answer = 0;
    let answer1 = 0;
    for (let i = 0; i < num_list.length; i += 2) {
        answer += num_list[i];
    }
    for (let j = 1; j < num_list.length; j += 2) {
        answer1 += num_list[j];
    }
    if (answer > answer1) {
        return answer;
    } else {
        return answer1;
    }
}
