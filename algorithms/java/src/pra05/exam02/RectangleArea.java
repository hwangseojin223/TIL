package pra05.exam02;

import java.util.*;

public class RectangleArea {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Rectangle rect = new Rectangle();
		Scanner scanner = new Scanner(System.in);
		System.out.print(">> ");
		
		rect.width = scanner.nextInt();
		rect.height = scanner.nextInt();
		
		System.out.println("사각형의 면적은 "+ rect.getArea());
		
		scanner.close();
		
		

	}

}
