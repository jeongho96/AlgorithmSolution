class Solution {
    public int solution(String A, String B) {
        // A와 B의 길이가 다르면 -1 반환
        if (A.length() != B.length()) {
            return -1;
        }

        // A와 B가 처음부터 같으면 0번 회전한 것이므로 0 반환
        if (A.equals(B)) {
            return 0;
        }

        // A를 한 칸씩 밀면서 B와 같은지 확인
        String rotated = A;
        for (int i = 1; i <= A.length(); i++) {
            rotated = rotated.substring(rotated.length() - 1) + rotated.substring(0, rotated.length() - 1); // 한 칸 회전
            if (rotated.equals(B)) {
                return i; // 몇 번 회전했는지 반환
            }
        }

        return -1;  // 끝까지 회전해도 같지 않으면 -1 반환
    }
}