import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        List<Integer> dayLeft = new ArrayList<>();

        for(int i = 0; i < progresses.length; i++) {
            dayLeft.add((int) Math.ceil((100.0 - progresses[i]) / speeds[i]));
        }

        int count = 1;
        int checkNumber = dayLeft.get(0);

        for(int i = 1; i < dayLeft.size(); i++) {
            // 다음 작업이 현재 작업보다 늦게 완료될 때
            if(checkNumber >= dayLeft.get(i)) {
                count++;
            } else {
                answer.add(count); // 현재 count를 저장
                count = 1; // 새로운 count 초기화
                checkNumber = dayLeft.get(i);
            }
        }

        // 마지막 남아 있는 count 추가
        answer.add(count);

        return answer.stream()
                .mapToInt(i -> i).toArray();
    }
}