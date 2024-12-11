import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, List<String>> clothesMap = new HashMap<String, List<String>>();

        for(int i = 0; i < clothes.length; i++){
            addClothing(clothesMap, clothes[i][1], clothes[i][0]);
        }

        int answer = clothesMap.values().stream()
                .mapToInt(list -> list.size() + 1)
                .reduce(1, (a,b) -> a * b);

        return answer - 1;
    }
    
    // 카테고리에 옷을 추가하는 메서드
    private static void addClothing(Map<String, List<String>> map, String category, String item) {
        // 해당 카테고리의 리스트가 없으면 새로 생성
        map.putIfAbsent(category, new ArrayList<>());

        // 카테고리에 아이템 추가
        map.get(category).add(item);
    }
}