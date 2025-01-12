package pra09.exam03;

public class InterfaceEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SmartPhone sp = new SmartPhone();
		
		MobilePhoneInterface mp = sp;
		mp.sendCall();
		mp.receiveSMS();
		
		MP3Interface mp3 = sp;
		mp3.play();
		
		System.out.println("3과5를 더하면 "+ sp.calculate(3,5));
		sp.schedule();
	}

}
