package pra06.exam01;

public class Calculator {
	static int abs(int x) {
		if (x>=0) {
			return x;
		}
		else {
			return -x;
		}
	}
	static int max(int x, int y) {
		if (x>y) {
			return x;
		}
		else {
			return y;
		}
	}
	static int min(int x, int y) {
		if (x>y) {
			return y;
		}
		else {
			return x;
		}
	}

}
