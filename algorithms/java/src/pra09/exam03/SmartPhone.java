package pra09.exam03;

public class SmartPhone extends PDA implements MobilePhoneInterface, MP3Interface {
	@Override
	public void sendCall() {
		System.out.println("따르릉따르릉~~");
	}
	
	@Override
	public void receiveCall() {
		System.out.println("전화왔어요 ");
	}
	
	@Override
	public void sendSMS() {
		System.out.println("문자보내기 ");
	}
	
	@Override
	public void receiveSMS() {
		System.out.println("문자왔어요 ");
	}
	
	@Override
	public void play() {
		System.out.println("음악 연주합니다.");
	}
	
	@Override
	public void stop() {
		System.out.println("음악 멈춥니다.");
	}
	public void schedule() {
		System.out.println("일정 관리");
	}
	
	}
	

}
