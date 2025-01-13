package pra13.exam01;

import java.util.List;
import java.util.*;

public class IteratorEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Integer> v = new Vector<Integer>();
		v.add(5);
		v.add(4);
		v.add(-1);
		v.add(2, 100);
		
		Iterator<Integer> iterator = v.iterator();
		
		int sum = 0;
		
		while(iterator.hasNext()) {
			int element = iterator.next();
			sum += element;
			System.out.println(element);
		}
		System.out.println("벡터에 있는 정수 합 : "+sum);

	}

}
