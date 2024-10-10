import java.util.ArrayList;
import java.util.List;

class Solution {
    public String[] solution(String my_str, int n) {
        List<String> list = new ArrayList<String>();


        for(int i = 0; i < my_str.length(); i += n){
            if(i + n > my_str.length()){
                list.add(my_str.substring(i, my_str.length()));
                break;
            }
            
            list.add(my_str.substring(i, i+n));
        }

        return list.toArray(new String[list.size()]);
    }
}