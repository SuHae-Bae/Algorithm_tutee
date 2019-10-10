// 백준 1620
// 포켓몬마스터 이다솜
import java.io.*;
import java.util.*;

public class back1620 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        HashMap<String, Integer> maps = new HashMap<>();
        String Arr[] = new String[N];

        for (int i = 0; i < N; i++){
            String s = sc.next();
            Arr[i] = s;
            maps.put(s, i + 1);
        }

        for (int i = 0; i < M; i++){
            if(sc.hasNextInt()){
                System.out.println(Arr[sc.nextInt() - 1]);
            } else {
                System.out.println(maps.get(sc.next()));
            }
        }
    }
}