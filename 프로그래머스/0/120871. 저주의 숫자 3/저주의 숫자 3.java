class Solution {
    public int solution(int n) {
        int answer = 0;
    int count = 0;
    
    for (int i = 1; count < n; i++) {
        if (i % 3 == 0 || String.valueOf(i).contains("3")) {
            continue;  // 3의 배수이거나 숫자 '3'이 포함된 경우 건너뛰기
        }
        count++;  // 유효한 숫자일 경우 count 증가
        answer = i;  // 현재 숫자를 answer에 저장
    }
    
    return answer;
    }
}