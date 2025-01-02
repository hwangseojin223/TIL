package pra04.exam01;

import java.util.Scanner;

public class MaxNumber {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int intArray[] = new int[5];
		
		System.out.println("양수 5개를 입력하세요.");
		
		for (int i=0; i<5; i++) {
			int tmp = scanner.nextInt();
			intArray[i] = tmp;
		}
		int max = intArray[0];
		for (int i=0; i<5; i++){
			if (intArray[i] > max) {
				max = intArray[i];
			}
		}
		System.out.printf("가장 큰 수는 %d입니다,",max);
		
		scanner.close();
	}

}
