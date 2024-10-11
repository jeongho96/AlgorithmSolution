class Solution {
    public int solution(String[] spell, String[] dic) {
                       int answer = 2;
        // spell에 있는 모든 소문자를 사용한 단어가 있으면 1, 없으면 2


        for(int i = 0; i < dic.length; i++){
            int count = 0;
             for(int j = 0; j < spell.length; j++){
                 if(dic[i].contains(spell[j])){
                     count++;
                 }
                 if(count == spell.length) {
                     answer = 1;
                     break;
                 }
             }
        }

        return answer;
    }
}