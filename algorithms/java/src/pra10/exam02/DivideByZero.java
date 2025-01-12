package pra10.exam02;

import java.util.Scanner;

public class DivideByZero {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int dividend;
		int divisor;
		
		System.out.print("나뉨수를입력하시오: ");
		dividend = scanner.nextInt();
		System.out.print("나눗수를입력하시오: ");
		divisor = scanner.nextInt();
		System.out.println(dividend/divisor);
		scanner.close();
		
		

	}

}
