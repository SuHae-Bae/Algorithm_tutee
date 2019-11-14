import java.util.Scanner;

public class Q2191110 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] domino = new int[n+1];

        domino[0] = 0;
        domino[1] = 1;

        for(int i = 2; i <= n; i++){
            domino[i] = domino[i - 1] + domino[i - 2];
        }

        System.out.println(domino[n]);
    }

}
