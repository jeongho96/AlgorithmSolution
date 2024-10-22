
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] solution(int[] arr) {
         List<Integer> list = new ArrayList<>();

        int i = 0;
        while (i < arr.length) {
            if (list.isEmpty()) {
                list.add(arr[i]);
                i++;  // 다음 값으로 이동
            } else if (list.get(list.size() - 1) < arr[i]) {
                list.add(arr[i]);
                i++;  // 다음 값으로 이동
            } else {
                list.remove(list.size() - 1);  // 마지막 값 삭제
            }
        }

        return list.stream().mapToInt(num -> num).toArray();
    }
}