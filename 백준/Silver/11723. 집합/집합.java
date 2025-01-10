


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int m = Integer.parseInt(br.readLine());
        int set = 0; // 집합을 나타낼 정수

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            int x = 0;

            if (st.hasMoreTokens()) {
                x = Integer.parseInt(st.nextToken());
            }

            switch (command) {
                case "add":
                    set |= (1 << (x - 1)); // x를 추가
                    break;
                case "remove":
                    set &= ~(1 << (x - 1)); // x를 제거
                    break;
                case "check":
                    sb.append((set & (1 << (x - 1))) != 0 ? 1 : 0).append("\n"); // x의 포함 여부 확인
                    break;
                case "toggle":
                    set ^= (1 << (x - 1)); // x를 토글
                    break;
                case "all":
                    set = (1 << 20) - 1; // {1, 2, ..., 20}으로 설정
                    break;
                case "empty":
                    set = 0; // 공집합으로 초기화
                    break;
            }
        }

        System.out.print(sb);
    }
}
