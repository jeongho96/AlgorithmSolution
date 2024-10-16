import java.util.Arrays;
import java.util.List;
class Solution {
    public String solution(String[] id_pw, String[][] db) {
        for (String[] entry : db) {
        if (entry[0].equals(id_pw[0])) { // ID가 일치할 경우
            if (entry[1].equals(id_pw[1])) { // 비밀번호가 일치할 경우
                return "login"; // 로그인 성공
            } else {
                return "wrong pw"; // 비밀번호가 틀림
            }
        }
    }
    return "fail"; // ID가 없음
    }
}