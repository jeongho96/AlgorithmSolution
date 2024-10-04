
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;


public class Main {

    public static int solution(String phoneNumber){
        int answer = 0;
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        // 배열을 통해 문자 범위별로 매핑
        char[][] groups = {
                {'A', 'B', 'C'},  // 2에 해당하는 문자들
                {'D', 'E', 'F'},  // 3에 해당하는 문자들
                {'G', 'H', 'I'},  // 4에 해당하는 문자들
                {'J', 'K', 'L'},  // 5에 해당하는 문자들
                {'M', 'N', 'O'},  // 6에 해당하는 문자들
                {'P', 'Q', 'R', 'S'},  // 7에 해당하는 문자들
                {'T', 'U', 'V'},  // 8에 해당하는 문자들
                {'W', 'X', 'Y', 'Z'}   // 9에 해당하는 문자들
        };

        // 반복문을 통해 각 그룹의 문자를 맵에 추가
        for (int i = 0; i < groups.length; i++) {
            for (char c : groups[i]) {
                map.put(c, i + 3);  // 2부터 시작하는 번호로 매핑
            }
        }

        for(char c : phoneNumber.toCharArray()){
            answer += map.get(c);
        }


        return answer;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        System.out.println(solution(s));
    }
}