class Solution {
    // 암호화된 문자열 cipher, cipher의 진짜 암호는 code 배수 번째 글자
    // 예를 들어 "pfqallllabwaoclk" , code = 2 면 fallback
    // 해독된 암호 문자열을 return
    public String solution(String cipher, int code) {
        StringBuilder builder = new StringBuilder();
        // 시작이 code번째부터이므로 인덱스 조정
        for(int i = code - 1; i < cipher.length(); i += code){
            builder.append(cipher.charAt(i));
        }
        return builder.toString();
    }
}