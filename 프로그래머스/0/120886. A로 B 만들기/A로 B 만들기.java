class Solution {
    public int solution(String before, String after) {
        int count = 0;
        for(int i = 0; i < before.length(); i++){
            if(after.contains(before.charAt(i) + "")){
                count++;
                after = after.replaceFirst(before.charAt(i) + "", "");
            }
        }

        return count == before.length() ? 1 : 0;
    }
}