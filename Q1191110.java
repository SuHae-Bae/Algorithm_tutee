import java.util.Arrays;
import java.util.Scanner;
public class Q1191110 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b;
        int n = sc.nextInt();
        int Mat[][] = new int[n][n];
        int c[][] = new int [n][n];
        int i, j;
        for(a = 0; a < n; a++) {
            for(b = 0; b < n; b++){
                Mat[a][b] = sc.nextInt();
            }
        }
        c[0][0] = Mat[0][0];
        for(i = 1; i < n; i++){
            c[i][0] = Mat[i][0] + c[i - 1][0];
        }
        for(j = 1; j < n; j++){
            c[0][j] = Mat[0][j] + c[0][j - 1];
        }
        for(i = 1; i < n; i++){
            for(j = 1; j < n; j++){
                c[i][j] = Mat[i][j] + MAX(c[i - 1][j], c[i][j-1], c[i][j-1]);
            }
        }

        System.out.println(c[n-1][n-1]);

    }

    public static int MAX(int x, int y, int z){
        if (x >= y && x >= z) {
            return x;
        } else if (y >= x && y >= z) {
            return y;
        } else {
            return z;
        }

    }

}
