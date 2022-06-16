package com.mycompany.assignment6;

import java.util.Scanner;
class InvalidDLException extends Exception {
	
}
class InvalidAdhaarException extends Exception {

}
class InvalidDetails extends Exception {
	
}
public class JobWindow {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		try {
			boolean flag1 = false, flag2 = false;
			System.out.print("Enter DL: ");
			int dl = sc.nextInt();
			System.out.print("Enter Adhaar: ");
			int adhaar = sc.nextInt();
			sc.close();

			if(dl>20000 && dl<30000)
				flag1 = true;
			
			if(adhaar<500000000 && adhaar>400000000)
				flag2 = true;
			
			if(flag1 && flag2)
				System.out.println("You have applied for job successfully");
			else if(flag1 && !flag2)
				throw new InvalidAdhaarException();
			else if(!flag1 && flag2)
				throw new InvalidDLException();
			else
				throw new InvalidDetails();
		}
		catch(InvalidDLException e) {
			System.out.println("Wrong DL number.");
		}
		catch(InvalidAdhaarException e) {
			System.out.println("Wrong Adhaar number.");
		}
		catch(InvalidDetails e) {
			System.out.println("Wrong DL and Adhaar details.");
		}
	}

}
