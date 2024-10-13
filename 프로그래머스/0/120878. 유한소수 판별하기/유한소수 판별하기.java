import java.util.*;

class Solution {
    public int solution(int a, int b) {
        // 최대공약수로 기약 분수 만들기
        int gcdValue = gcd(a, b);
        a /= gcdValue;
        b /= gcdValue;

        // 분모의 소인수 중 2와 5만 있는지 확인
        b = removeFactor(b, 2);  // 2로 나누어 떨어지는 부분 제거
        b = removeFactor(b, 5);  // 5로 나누어 떨어지는 부분 제거

        // 만약 2와 5 외의 소인수가 남아있다면 유사 소수가 아님
        return (b == 1) ? 1 : 2;
    }

    // 최대공약수 계산 (유클리드 호제법)
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    // 특정 소인수를 제거하는 함수
    private int removeFactor(int num, int factor) {
        while (num % factor == 0) {
            num /= factor;
        }
        return num;
    }
}
