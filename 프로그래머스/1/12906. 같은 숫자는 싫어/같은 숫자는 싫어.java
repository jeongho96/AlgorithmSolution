import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> numberList = new ArrayList<>();

        int checkNumber = arr[0];

        // 연속된 숫자일 경우 제거하고 반환하기
        for(int i = 0; i < arr.length; i++){

            if(arr[i] == checkNumber && i != 0){
                continue;
            }

            numberList.add(arr[i]);
            checkNumber = arr[i];

        }

        int[] answer = new int[numberList.size()];
        for(int i = 0; i < numberList.size(); i++){
            answer[i] = numberList.get(i);
        }

        return answer;
    }
}