import java.util.Scanner;

class SophisticatedSalary{
	public static void main(String []args){
		
		Scanner scan = new Scanner(System.in);
		String inputString = scan.nextLine();
		char arr[] = inputString.toCharArray();

		for (char item : arr){
			System.out.println("Next character is:" + item);
		}
	}
}