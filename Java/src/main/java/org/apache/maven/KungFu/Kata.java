package org.apache.maven.KungFu;

import com.google.common.base.Joiner;
import com.google.common.collect.Lists;
import com.google.common.collect.Range;
import com.google.common.collect.DiscreteDomain;
import com.google.common.collect.ContiguousSet;
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
    
    public static long SumSeries(long n) {
    	long result = 0;
        for(long i=0;i<n;i++)
            result += i;
        return result;
    }
    /*
    public static int BecomeImmortalO(int m, int n, int l, int t) {
    	int rowvalue = SumSeries(m);
    	int rowsubtract = l*(m-1);
        int row = rowvalue - rowsubtract;
        int total = row * n;
        //return total;
        return (SumSeries(m) - (l*(m-1))) * n;
    }
    */

    public static long BecomeImmortal(long n, long m, long k, long newp) {
    	long rowvalue = SumSeries(n);
    	long rowsubtract = k*(n-1);
    	long row = rowvalue - rowsubtract;
    	long total = row * m;

		System.out.println(rowvalue);
		System.out.println(rowsubtract);
		System.out.println(row);
		System.out.println(total);
		System.out.println("----");
		
    	return total % newp;
    }
    
    public static long BecomeImmortal1(long n, long m, long k, long newp) {
        return Long.valueOf(  ((SumSeries(n) - (k*(n-1))) * m) % newp );
    }
}


