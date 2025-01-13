package pra12.exam01;

import java.awt.Toolkit;

public class TestThread {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Thread th = new TimerThread();
		th.start();
		
		
		Toolkit toolkit = Toolkit.getDefaultToolkt();
		while(true) {
			toolkit.beep();
			try {
				Thread.sleep(1000);
			}catch(Exceiption e) {}
		}
			
		
		

	}

}
