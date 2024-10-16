class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
for(int i = 0; i < babbling.length; i++) {
    int check = babbling[i].length();
    for(int j = 0; j < babbling[i].length();) {
        if(babbling[i].charAt(j) == 'a' && j + 3 <= babbling[i].length() && babbling[i].substring(j, j + 3).equals("aya")) {
            check -= 3;
            j += 3; // 인덱스를 3만큼 이동
        } 
        else if(babbling[i].charAt(j) == 'y' && j + 2 <= babbling[i].length() && babbling[i].substring(j, j + 2).equals("ye")) {
            check -= 2;
            j += 2; // 인덱스를 2만큼 이동
        } 
        else if(babbling[i].charAt(j) == 'm' && j + 2 <= babbling[i].length() && babbling[i].substring(j, j + 2).equals("ma")) {
            check -= 2;
            j += 2; // 인덱스를 2만큼 이동
        } 
        else if(babbling[i].charAt(j) == 'w' && j + 3 <= babbling[i].length() && babbling[i].substring(j, j + 3).equals("woo")) {
            check -= 3;
            j += 3; // 인덱스를 3만큼 이동
        } 
        else {
            j++; // 아무 것도 안 맞으면 인덱스를 1만큼 이동
        }
    }
    if(check == 0) {
        answer++;
    }
}

return answer;
    }
}