package pra12.exam01;


public class TimerThread extends Thread {
	int n = 0;
	@Override
	public void run() {
		while (true){
			System.out.println(n);
			n++;
			try {
				Thread.sleep(10000);
			}catch(InterruptedException e) {return;}
		}
	}

}
