package pra04.exam03;

public class NonSquareArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[][] array = new int[4][];
		array[0] = new int[3];
		array[1] = new int[2];
		array[2] = new int[3];
		array[3] = new int[2];
		
		for (int i=0; i<array.length; i++) {
			int tmp = (i+1)*10;
			for (int k=0; k<array[i].length; k++) {
				int sum = tmp + k; 
				System.out.print(sum+" ");
			}
			System.out.println();
		}
		
	}

}
