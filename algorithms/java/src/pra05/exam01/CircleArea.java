package pra05.exam01;

//import java.util.*;


public class CircleArea {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
		Scanner scan = new Scanner(System.in);
		int radius = scan.nextInt();
		String circleName = scan.next();
		
		Circle circle = new Circle(radius, circleName);
		double areaCircle = circle.areaCircle(radius);
		System.out.printf("반지름(%d) : %s의 면적은 %.2f", radius, circleName, areaCircle);
		*/
		
		
		Circle circle1 = new Circle(10, "자바피자");
		double areaCircle = circle1.areaCircle();
		System.out.printf("반지름(%d) : %s의 면적은 %.2f", circle1.radius, circle1.circleName, areaCircle);
		
	}

}
