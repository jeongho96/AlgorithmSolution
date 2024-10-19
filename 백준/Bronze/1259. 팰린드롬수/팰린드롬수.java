
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

import java.util.List;


public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = " ";
        List<String> nums = new ArrayList<>();
        while(s.charAt(0) != '0') {
            s = br.readLine();
            nums.add(s.trim());
        }
        // 0 제거
        nums.remove(nums.size() - 1);

        for(int i = 0; i < nums.size(); i++) {
            for(int j = 0; j < nums.get(i).length(); j++) {
                if(nums.get(i).charAt(j) != nums.get(i).charAt(nums.get(i).length() - 1 - j)) {
                    System.out.println("no");
                    break;
                }
                else if(j == nums.get(i).length() - 1) {
                    System.out.println("yes");
                }
            }
        }

    }
}
