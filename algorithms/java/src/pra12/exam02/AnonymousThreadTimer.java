package pra12.exam02;

import java.awt.Toolkit;

public class AnonymousThreadTimer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Thread th = new Thread() {
			int n =0;
			@Override
			public void run() {
				while(true) {
					System.out.println(n);
					n++;
					try {
						Thread.sleep(10000);
					}catch(InterruptedException e) {return;}
				}
			}
		};
		th.start();
		
		
		Toolkit toolkit = Toolkit.getDefaultToolkit();
		while(true) {
			toolkit.beep();
			try {
				Thread.sleep(1000);
			}catch(Exception e) {}
		}
	}

}
