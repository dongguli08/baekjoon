    function solution(num_list) {
    var answer = [];
    let last1 = num_list[num_list.length - 1];  // 배열의 마지막 요소를 참조
    let last2 = num_list[num_list.length - 2];  // 배열의 두 번째 마지막 요소를 참조
    
    if (last1 > last2) {
        num_list.push(last1 - last2);  // 마지막 요소가 두 번째 마지막 요소보다 크면 차이를 추가
    } else {
        num_list.push(last1 * 2);  // 그렇지 않으면 마지막 요소의 두 배를 추가
    }  
    
    return num_list;
}
