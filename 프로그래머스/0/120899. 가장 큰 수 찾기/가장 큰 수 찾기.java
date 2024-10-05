class Solution {
    public int[] solution(int[] array) {
        int[] answer = new int[2]; // 값과 인덱스 2개뿐이니까

        int maxNumber = Integer.MIN_VALUE;
        int maxIndex = 0;
        for(int i = 0; i < array.length; i++){
            if(array[i] > maxNumber){
                maxNumber = array[i];
                maxIndex = i;
            }
        }
        answer[0] = maxNumber;
        answer[1] = maxIndex;

        return answer;
    }
}