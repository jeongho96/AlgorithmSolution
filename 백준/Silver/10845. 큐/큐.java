
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        CustomQueue queue = new CustomQueue();

        for(int i = 0; i < T; i++) {
            // 여러 값 한 줄 입력받기
            StringTokenizer st = new StringTokenizer(br.readLine());
            String input = st.nextToken();
            switch(input) {
                case "push":
                    int value = Integer.parseInt(st.nextToken());
                    queue.push(value);
                    break;
                case "pop":
                    System.out.println(queue.pop());
                    break;
                case "size":
                    System.out.println(queue.size());
                    break;
                case "empty":
                    System.out.println(queue.empty());
                    break;
                case "front":
                    System.out.println(queue.front());
                    break;
                case "back":
                    System.out.println(queue.back());
                    break;
            }

        }

    }
}


class CustomQueue{
    private List<Integer> list;

    public CustomQueue() {
        list = new ArrayList<>();
    }

    public void push(int X){
        list.add(X);
    }

    public int pop(){
        return (list.size() == 0) ? -1 : list.remove(0);
    }

    public int size(){
        return list.size();
    }

    public int empty(){
        return (list.size() == 0) ? 1 : 0;
    }

    public int front(){
        return (list.size() == 0) ? -1 : list.get(0);
    }

    public int back(){
        return (list.size() == 0) ? -1 : list.get(list.size()-1);
    }
}