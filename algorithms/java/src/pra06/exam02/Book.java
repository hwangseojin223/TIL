package pra06.exam02;

public class Book {
	String title;
	String author;
	Book() {
		this.title="";
		this.author="";
	}
	
	Book(String title, String author){
		this.title = title;
		this.author = author;
		
	}
	Book (String title){
		this.title = title;
		this.author = "작자미상";
	}
	void show() {
		System.out.println("제목: " + title + ", 작가: " + author);
	}
}
