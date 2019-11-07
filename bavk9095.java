package Algorithm;
import java.util.Scanner;

public class back9095 {
    public static void main(String[] args) {
        int[] arr = new int[11]; //n < 11이므로
        int T, n; // T = 입력받을 테스트갯수, n = 123으로 나타낼 숫자
        Scanner scanner = new Scanner(System.in);


        //arr[n]에 n의 경우의 수를 집어넣을거임
        arr[0] = 0; // 입력받은 수가 0이면 경우의 수는 0
        arr[1] = 1; // 입력받은 수가 1이면 경우의 수는 1
        arr[2] = 2; // 입력받은 수가 2이면 경우의 수는 2
        arr[3] = 4; // 입력받은 수가 3이면 경우의 수는 4
        T = scanner.nextInt();
        for(int i = 0; i < T; i++) {
            n = scanner.nextInt(); // T번 동안 n을 입력받음
            for(int j = 4; j <= n; j++){ // 1, 2, 3은 정해져있으니까 4부터 생각함
                arr[j] = arr[j-1] + arr[j-2] + arr[j-3];
            }
            System.out.println(arr[n]);
        }
        scanner.close();
    }
}
