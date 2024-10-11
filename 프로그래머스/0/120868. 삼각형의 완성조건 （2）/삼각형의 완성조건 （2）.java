class Solution {
    public int solution(int[] sides) {
        int result = 0;
        int min = Math.min(sides[0], sides[1]);
        int max = Math.max(sides[0], sides[1]);
        

        result += max - (max - min + 1);
        

        result += (max + min) - max;
        

        return min * 2 - 1;

    }
}