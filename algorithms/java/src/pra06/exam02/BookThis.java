package pra06.exam02;

public class BookThis {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Book emptyBook = new Book();
		emptyBook.show();
		Book littlePrince = new Book("어린왕자", "생텍쥐페리");
		littlePrince.show();
		Book loveStory = new Book("춘향전");
		loveStory.show();

	}

}
