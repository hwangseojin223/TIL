package pra01.exam03;

import java.util.Scanner;

public class LeibnizFormula {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		System.out.print("반복횟수: ");
		int loop_count = scan.nextInt();
		double numerator = 4.0;
		double denominator = 1.0;
		double sum = 0.0;
		
		while(loop_count > 0) {
			sum = sum + numerator / denominator;
			numerator = -1.0 * numerator;
			denominator = denominator + 2.0;
			--loop_count;
		}
		System.out.printf("Pi = %.16f", sum);
		scan.close();

	}

}
