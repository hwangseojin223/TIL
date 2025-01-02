package pra01.exam01;

import java.util.Scanner;

public class ArithmeticOperator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		System.out.print("정수를 입력하세요: ");
		int time = scanner.nextInt();
		
		int hour = time / 60 / 60;
		int minute = time / 60 % 60;
		int second = time % 60;
		
		System.out.printf("%d초는 %d시간, %d분, %d초입니다.", time, hour, minute, second);
		
		scanner.close();
	}

}
