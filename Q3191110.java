import java.util.Scanner;

public class Q3191110 {
    static int[][] C = new int[1000][1000];
    static String[][] B  = new String[1000][1000];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String x = sc.next();
        String y = sc.next();
        int m = x.length();
        int n = y.length();
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (x.toCharArray()[i - 1] == y.toCharArray()[j - 1]) {
                    C[i][j] = C[i - 1][j - 1] + 1;
                    B[i][j] = "D";
                } else {
                    if (C[i-1][j] >= C[i][j - 1]){
                        C[i][j] = C[i - 1][j];
                        B[i][j] = "U";
                    }
                    else{
                        C[i][j] = C[i][j - 1];
                        B[i][j] = "L";
                    }
                }
            }
        }
        System.out.println(C[m][n]);
    }
}