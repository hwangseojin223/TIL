package pra04.exam02;

import java.util.Scanner;

public class ForEach {
	public static void main(String[] args) {
		String names[] = {"사과", "배", "바나나", "체리", "딸기", "포도"};
		
		int num = 0;
		
		for (String name: names) {
				num += 1;
				System.out.printf("%d-%s ", num, name);
			
		}
		
	}

}
