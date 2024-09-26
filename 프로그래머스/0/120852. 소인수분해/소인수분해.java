import java.util.ArrayList;
import java.util.List;


class Solution {
    public int[] solution(int n) {
        List<Integer> primeFactors = new ArrayList<>();
        
        // 2로 나눌 수 있을 때까지 나누기
        while (n % 2 == 0) {
            primeFactors.add(2);
            n /= 2;
        }
        
        // 3부터 √n까지의 홀수에 대해서 나누기 시도
        for (int i = 3; i * i <= n; i += 2) {
            while (n % i == 0) {
                primeFactors.add(i);
                n /= i;
            }
        }
        
        // n이 2 이상의 소수로 남아있다면 그것도 추가
        if (n > 2) {
            primeFactors.add(n);
        }
        
        return primeFactors.stream().distinct().mapToInt(i -> i).toArray();
    }
}