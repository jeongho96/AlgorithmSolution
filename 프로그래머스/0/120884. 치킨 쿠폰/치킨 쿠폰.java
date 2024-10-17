class Solution {
    public int solution(int chicken) {
        int totalChicken = 0;

        while(chicken >= 10){
            int newChicken = chicken / 10;
            totalChicken += newChicken;
            chicken = (chicken % 10) + newChicken;
        }

        return totalChicken;

    }
}