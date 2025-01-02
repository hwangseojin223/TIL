package pra01.exam02;

import java.util.Scanner;

public class GreatestCommonDivisor {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x, y, r;
		System.out.print("두개의 정수를 입력하시오(큰수, 작은수): ");
		Scanner scan = new Scanner(System.in);
		
		x = scan.nextInt();
		y = scan.nextInt();
		r = y;
		while(y>=r) {
			if (x%r == 0 && y%r == 0) {
				break;
			}
			r--;
				
		}
		System.out.printf("최대 공약수는 %d", r);
		scan.close();
	}

}
