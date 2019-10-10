//백준 10815
//상근이

import java.io.*;

import java.util.*;



public class back10815 {



    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));



        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i< n; i++) {

            arr[i] = Integer.parseInt(st.nextToken());

        }


        //오름차순 정렬
        Arrays.sort(arr);



        int size = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());

        StringBuilder ans = new StringBuilder();

        for (int i = 0; i< size; i++) {

            int num = Integer.parseInt(st.nextToken());

            if (Arrays.binarySearch(arr, num) >= 0) ans.append(1);

            else ans.append(0);

            ans.append(" ");

        }

        System.out.print(ans);

    }



}
