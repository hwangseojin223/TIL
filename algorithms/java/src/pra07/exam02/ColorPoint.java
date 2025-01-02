package pra07.exam02;

public class ColorPoint extends Point {
	String color;
	
	ColorPoint(int x, int y, String color){
		super(x, y);
		this.color = color;
	}
	
	void showColorPoint() {
		System.out.println(color+"("+x+","+y+")");
	}

}
