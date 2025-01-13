package pra12.exam04;

import java.awt.Toolkit;

public class AnonymousRunnableTimer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Thread th = new Thread(new Runnable() {
			int n =0;
			@Override
			public void run() {
				while(true) {
					System.out.println(n);
					n++;
					try {
						Thread.sleep(1000);
					}catch(InterruptedException e) {
						return;
					}
				}
			}
		});
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
