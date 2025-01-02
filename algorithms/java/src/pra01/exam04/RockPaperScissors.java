package pra01.exam04;
import java.util.*;

public class RockPaperScissors {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		System.out.print("가위(0), 바위(1), 보(2): ");
		int user = sc.nextInt();
		Random ran = new Random();
		int computer = ran.nextInt(3);
		
		if (user == 0) {
			if (computer == 1) {
				System.out.printf("인간: %d 컴퓨터: %d 컴퓨터 승리" , user, computer);
			}else if (computer == 2) {
				System.out.printf("인간: %d 컴퓨터: %d 인간 승리" , user, computer);
			}
		}
		else if (user == 1) {
			if (computer == 0) {
				System.out.printf("인간: %d 컴퓨터: %d 인간 승리" , user, computer);
			}
			else if (computer == 2) {
				System.out.printf("인간: %d 컴퓨터: %d 컴퓨터 승리" , user, computer);
			}
		}
		else if (user == 2) {
			if (computer == 0) {
				System.out.printf("인간: %d 컴퓨터: %d 컴퓨터 승리" , user, computer);
			}
			else if (computer == 1){
				System.out.printf("인간: %d 컴퓨터: %d 인간 승리" , user, computer);
			}
		}
	}

}
