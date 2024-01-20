import java.util.Scanner;

class Challenge{

	static String longestPalSubstr(String s) {
		int n = s.length();
		int start = 0, end = 1;
		int low, hi;

		// Traverse the input string
		for (int i = 0; i < n; i++) {

			low = i - 1;
			hi = i;

			while (low >= 0 && hi < n && s.charAt(low) == s.charAt(hi)) {
				if (hi - low + 1 > end) {
					start = low;
					end = hi - low + 1;
				}
				low--;
				hi++;
			}

			low = i - 1;
			hi = i + 1;

			while (low >= 0 && hi < n && s.charAt(low) == s.charAt(hi)) {
				if (hi - low + 1 > end) {
					start = low;
					end = hi - low + 1;
				}
				low--;
				hi++;
			}
		}

		// Return output Substring
		return s.substring(start, start+end);
	}

	// Driver code
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the string: ");
		String string =input.next();
		// String s = "forgeeksskeegfor";  
        //String s = "geeks";
		System.out.println("Longest palindrome substring is:"+longestPalSubstr(string));
	}
}
