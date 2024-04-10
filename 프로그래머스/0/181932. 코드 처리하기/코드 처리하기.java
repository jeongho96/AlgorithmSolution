class Solution {
    public String solution(String code) {
        StringBuilder ret = new StringBuilder();
        boolean mode = false;
        for(int i = 0; i < code.length();i++){
            char a = code.charAt(i);
            if(mode == false){
                if(!(a == '1') && (i % 2 == 0)){
                    ret.append(a);
                }
            }
            else if(mode == true){
                if(!(a == '1') && (i % 2 != 0)){
                    ret.append(a);
                }
            }
            
    
                mode = (a =='1') ? !mode : mode;
        }
        
        String answer = ret.toString();
        
        if (answer.trim().equals(""))
            answer = "EMPTY";
        
        return answer;
    }
}