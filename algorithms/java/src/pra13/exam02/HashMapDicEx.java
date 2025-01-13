package pra13.exam02;

import java.util.*;

public class HashMapDicEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Map<String, String> dic = new HashMap<String, String>();
		
		dic.put("baby","아기");
		dic.put("love","사랑");
		dic.put("apple","사과");
		
		
		while(true) {
			Scanner sc = new Scanner(System.in);
			System.out.print("찾고 싶은 단어는? ");
			String word = sc.next();
			
			if(dic.containsKey(word)) {
				System.out.println(dic.get(word));
			}
			else if (word.equals("exit")){
				System.out.println("종료합니다.");
				break;
			}
			else {
				System.out.println(word+"는 없는 단어입니다.");
			}
		}
		

	}

}
