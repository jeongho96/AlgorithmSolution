import java.util.ArrayList;
import java.util.List;

class Solution {
    boolean solution(String s) {
        char[] array = s.toCharArray();
        List<Character> list = new ArrayList<Character>();

        if(array[0] == ')') return false;
        
        for(int i = 0; i < array.length; i++){
            if(array[i] == '(') list.add('(');
            else if(array[i] == ')' && list.size() > 0){
                list.remove(list.size() - 1);
            }

        }

        if(list.size() != 0) return false;


        return true;
    }
}