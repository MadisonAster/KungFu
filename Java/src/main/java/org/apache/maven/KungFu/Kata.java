package org.apache.maven.KungFu;

import com.google.common.base.Joiner;
import com.google.common.collect.Lists;
import java.util.List;

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
    
    public static String createPhoneNumber(int[] numbers) {
        String result = "";
        for(int i = 0; i < numbers.length; i++) {
            if (i == 0) {result += "(";}
            result += numbers[i];
            if (i == 2) {result += ") ";}
            if (i == 5) {result += "-";}
        }
        return result;
    }
    public static String ListJoin(String[] args) {
        List<String> myList = Lists.newArrayList(args);
        String result = Joiner.on(",").join(myList);
        return result;
    }
}