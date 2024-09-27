import java.util.Arrays;

class Solution {
    public int solution(int[] sides) {
        int answer = 0;

        // 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 한다.

        // 가장 길이가 긴 변을 구하기
        int max = Arrays.stream(sides).max().getAsInt();

        // sides의 값을 다 합치고 max를 뺸 값보다 max가 작아야한다.
        // 가능이면 1, 아니면 2
        if(max < Arrays.stream(sides).sum() - max){
            answer = 1;
        }
        else{
            answer = 2;
        }


        return answer;
    }
}