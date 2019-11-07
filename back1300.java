//package Algorithm;
//1300 k번째 수

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class back1300 {

    static int N;
    static long K;

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken()); //문제에선 3에 해당
        st = new StringTokenizer(br.readLine());
        K = Long.parseLong(st.nextToken()); // 문제에선 7에 해당

        //일차원 배열에 오름 차순으로 정렬할 때 k번째 수 구하기

        long s = 1, e = K, mid = 0, ans = 0;
        //s = 시작지점, e = 끝위치(k)
        while (s <= e) // parametric search
        {
            //mid값을 설정
            mid = (s + e) / 2;
            //갯수 = cnt
            long cnt = 0;

            for (int i = 1; i <= N; i++) {
                // 몫이 N보다 큰 경우에는 그 개수가 N개인 것과 동일하므로..
                // e보다 작은 숫자의 갯수 구하기
                cnt += min(N, mid / i);
            }
            if (cnt < K) s = mid + 1;
            else {
                e = mid - 1;
                ans = mid;
            }

        }
        System.out.println(ans);
    }

    public static long min(long a, long b) {
        return a > b ? b : a;
    }
}