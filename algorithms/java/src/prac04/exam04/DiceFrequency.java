package prac04.exam04;

//import java.util.*;

public class DiceFrequency {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		final int SIZE = 6;
		int freq[] =new int[SIZE];
		
		for (int i=0; i<10000; i++) {
			++freq[(int)(Math.random()*SIZE)];
			
		}
		System.out.println("==========");
		System.out.println("면 "+"\t"+"빈도 ");
		System.out.println("==========");
		
		for (int i=0;i<SIZE; i++) {
			System.out.println(" "+(i+1)+"\t"+freq[i]);
		}
		
		
	}

}
