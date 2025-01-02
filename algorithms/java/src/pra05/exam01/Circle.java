
package pra05.exam01;

public class Circle {
	int radius;
	String circleName;
	
	Circle(int radius, String circleName){
		this.radius = radius;
		this.circleName = circleName;
		
	}
	
	double areaCircle() {
		double areaCircle = 3.14 * (double)radius * (double)radius;
		return areaCircle;
	}
	
}
