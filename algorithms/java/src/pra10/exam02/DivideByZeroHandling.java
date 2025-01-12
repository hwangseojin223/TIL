package pra10.exam02;

import java.util.Scanner;

public class DivideByZeroHandling {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		
		while(true) {
			int dividend = scanner.nextInt();
			int divisor = scanner.nextInt();
			try {
				System.out.println(dividend/divisor);
				break;
			}
			catch(ArithmeticException e) {
				System.out.println("0으로 나눌 수 없다. 다시 입력하세요 ");
			}
		}
		scanner.close();

	}

}
