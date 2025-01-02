package pra07.exam01;

public class ColorPoint extends Point {
	String color;
	
	ColorPoint(){}
	
	void setColor(String color) {
		this.color = color;
	}
	
	void showColorPoint() {
		System.out.print(color);
		showPoint();
		// System.out.println(color+"("+x+","+y+")");
	}

}
