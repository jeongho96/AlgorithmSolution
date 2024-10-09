import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int solution(int n) {
        return (n % Math.sqrt(n) == 0 ? 1 : 2);
    }
}