package pra10.exam03;

public class TestThrow {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(readString());
		

	}
	public static String readString() {
		byte[] buf = new byte[100];
		System.out.println("문자열을 입력하시오 ");
		System.in.read(buf);
		return new String(buf);
	}

}
