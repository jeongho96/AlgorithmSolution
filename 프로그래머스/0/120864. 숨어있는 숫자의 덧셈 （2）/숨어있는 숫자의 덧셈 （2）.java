import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(String my_string) {
        int answer;
        List<Integer> numList = new ArrayList<Integer>();
        // 숫자가 아닌 문자는 다 공백으로 변경 후 공백 기준으로 문자열 배열 형성
        for(String c : my_string.replaceAll("[^0-9]", " ").trim().split(" ")) {
            if(c.isEmpty()){
                continue;
            }
            numList.add(Integer.parseInt(c));
        }

        answer = numList.stream().mapToInt(n -> n).sum();

        return answer;
    }
}