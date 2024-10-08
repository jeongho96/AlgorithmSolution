

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {


    public static boolean solution(String s){
        // 그룹 단어인지 확인하는 변수
        boolean[] appeared = new boolean[26]; // 알파벳의 등장 여부를 기록

        char prev = s.charAt(0); // 첫 문자
        appeared[prev - 'a'] = true; // 첫 문자는 등장했다고 표시

        for (int i = 1; i < s.length(); i++) {
            char curr = s.charAt(i);

            if (curr != prev) { // 이전 문자와 다르면
                if (appeared[curr - 'a']) { // 이미 등장한 문자라면 그룹 단어가 아님
                    return false;
                }
                appeared[curr - 'a'] = true; // 등장하지 않은 문자라면 등장 표시
            }
            prev = curr; // 이전 문자를 현재 문자로 업데이트
        }

        return true; // 조건을 만족하면 그룹 단어
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); // 단어의 개수 입력
        int count = 0;

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            if (solution(s)) { // 그룹 단어일 경우 카운트 증가
                count++;
            }
        }

        System.out.println(count); // 그룹 단어의 개수 출력
    }
}
