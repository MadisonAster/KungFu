public class Kata {
	public static int square(int x) {
		return x*x;
	}

	public static int countA(String word) {
		int count = 0;
		for(int i = 0; i < word.length(); i++) {
			if(word.charAt(i) == 'a' || word.charAt(i) == 'A') {
				count++;
			}
		}
		return count;
	}
	
	public static String fakeBin(String numberString) {
	    return numberString.replaceAll("[0-4]", "0").replaceAll("[5-9]", "1");
	}
	
	public static int dutyFree(int normPrice, int discount, int hol) {
		return (int) (hol / ((discount / 100.0) * normPrice));		
	}
	static int findSum(String str) {  
        String temp = "";
        int sum = 0;
        for(int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (Character.isDigit(ch))  
                temp += ch;
            else
            {
                sum += Integer.parseInt(temp);
                temp = "0";  
            }  
        }
        return sum + Integer.parseInt(temp);  
    }
    
	public static final String generateShape(int n) {
		return ("+".repeat(n)+"\n").repeat(n).trim();
    }
}


class Goals {
	  public static int laLigaGoals = 43;
	  public static int championsLeagueGoals = 10;
	  public static int copaDelReyGoals = 5;
	  
	  public static int totalGoals = laLigaGoals+
				                     championsLeagueGoals+
				                     copaDelReyGoals;
}