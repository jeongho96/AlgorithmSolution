class Solution {
    public long solution(String numbers) {
                StringBuilder answer = new StringBuilder();

        StringBuilder tempString = new StringBuilder();
        for (char c : numbers.toCharArray()) {
            tempString.append(c);

            // Check if tempString matches any number word
            switch (tempString.toString()) {
                case "zero":
                    answer.append("0");
                    tempString.setLength(0); // Reset tempString
                    break;
                case "one":
                    answer.append("1");
                    tempString.setLength(0); // Reset tempString
                    break;
                case "two":
                    answer.append("2");
                    tempString.setLength(0); // Reset tempString
                    break;
                case "three":
                    answer.append("3");
                    tempString.setLength(0); // Reset tempString
                    break;
                case "four":
                    answer.append("4");
                    tempString.setLength(0); // Reset tempString
                    break;
                case "five":
                    answer.append("5");
                    tempString.setLength(0); // Reset tempString
                    break;
                case "six":
                    answer.append("6");
                    tempString.setLength(0); // Reset tempString
                    break;
                case "seven":
                    answer.append("7");
                    tempString.setLength(0); // Reset tempString
                    break;
                case "eight":
                    answer.append("8");
                    tempString.setLength(0); // Reset tempString
                    break;
                case "nine":
                    answer.append("9");
                    tempString.setLength(0); // Reset tempString
                    break;
            }
        }

        return Long.parseLong(answer.toString());

    }
}