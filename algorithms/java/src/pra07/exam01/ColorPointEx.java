package pra07.exam01;

public class ColorPointEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Point p = new Point(); 	       // Point 객체 생성
        p.setPoint(1, 2); 		       // Point 클래스의 setPoint() 호출
        p.showPoint();

        ColorPoint cp = new ColorPoint();    // ColorPoint 객체 
        cp.setColor("red"); 		       // ColorPoint의 setColor() 호출
        cp.setPoint(3, 4); 		       // Point의 setPoint() 호출
        cp.showColorPoint(); 		       // 컬러와 좌표 출력
	}

}
