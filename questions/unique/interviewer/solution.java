import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

// Question here

// Create a function that counts the number of unique characters in a string

// Input: String
// Output: Integer

public class solution {
	 
	public int solution1(String str)
	{
		HashSet<Character> unique = new HashSet<Character>();
		for (Character character : str.toCharArray())
		{
			if (!unique.contains(character))
			{
				unique.add(character);
			}
		}
		return unique.size();
	}
	
	public static void main(String[] args) {
		String str = "aabb cC"; // 5 unique chars
		solution sol = new solution();
		System.out.println(sol.solution1(str));
	}
	
}
