import java.util.Arrays;

class Solution {
    public int[] solution(int[] numlist, int n) {
                        int[][] diffArray = new int[numlist.length][2];
        for (int i = 0; i < numlist.length; i++) {
            diffArray[i][0] = numlist[i];
            diffArray[i][1] = Math.abs(numlist[i] - n);
        }

        // 1번 인덱스(n과의 절대값 차이)를 기준으로 확인하고 난 뒤
        // 만약 값이 같으면 0번(실제 값)으로 비교
        Arrays.sort(diffArray, (a,b) -> {
            int diff = Integer.compare(a[1], b[1]);
            if(diff == 0){
                return Integer.compare(b[0], a[0]);
            }
            return diff;
        });

        // 배열 출력 확인용
//        for(int i = 0; i < diffArray.length; i++){
//            for(int j = 0; j < diffArray[0].length; j++){
//                System.out.printf("%d번 : %d \n", j,diffArray[i][j]);
//            }
//        }
        
        // 0번 인덱스만 map을 써서 배열로 반환
        return Arrays.stream(diffArray).mapToInt(a -> a[0]).toArray();
    }
}