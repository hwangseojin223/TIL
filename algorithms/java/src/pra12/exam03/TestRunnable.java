package pra12.exam03;

import java.awt.Toolkit;

public class TestRunnable {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Runnable Task = new TimerRunnable();
		Thread th = new Thread(Task);
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
