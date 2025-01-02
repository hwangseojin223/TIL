package pra01.exam04;

import java.util.*;

public class RockPaperScissors2 {
	final int SCISSOR = 0;
	final int ROCK = 1;
	final int PAPER = 2;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Random ran = new Random();
		
		System.out.print("가위(0), 바위(1), 보(2): ");
		int user = sc.nextInt();
		
		int computer = ran.nextInt(3);
		
		if (user == computer) {
			System.out.println("비김");
		}
		else if ((user == 0 && computer == 2) || (user == 1 && computer == 0) || (user == 2 && computer == 1))
			System.out.println("인간: " + user + " 컴퓨터: " + computer + "   인간 승리");

		else
			System.out.println("인간: " + user + " 컴퓨터: " + computer + "   컴퓨터 승리");
		
		sc.close();
			
	}
}
