package pra06.exam03;

public class Account {
	private String name;
	private int balance;
	
	// void : 메서드가 아무것도 반환하지 않을 
	public void setName (String name) {
		this.name = name;
	}
	
	public void setBalance (int balance) {
		if(balance <0) {
			this.balance=0;
			return;
		}
		this.balance = balance;
	}
	// 반환값이 있을때 
	public String getName() {
		return name;
	}
	
	public int getBalance() {
		return balance;
	}
	

}
