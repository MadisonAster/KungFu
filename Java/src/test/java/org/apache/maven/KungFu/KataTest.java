package org.apache.maven.KungFu;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;


/**
 * Unit test for simple App.
 */
public class KataTest 
    extends TestCase
{
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public KataTest( String testName )
    {
        super( testName );
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite()
    {
        return new TestSuite( KataTest.class );
    }
    
    public void test_square() {
    	assertEquals(25, Kata.square(5));
    }
    public void test_fakeBin1() {
		assertEquals("1100", Kata.fakeBin("6644"));
	}
    public void test_dutyFree() {
		//System.out.println(System.getProperty("java.vm.version"));
	    assertEquals(166, Kata.dutyFree(12,50,1000));
	    assertEquals(294, Kata.dutyFree(17,10,500));
	    assertEquals(357, Kata.dutyFree(24,35,3000));
	    assertEquals(20, Kata.dutyFree(1400,35,10000));
	    assertEquals(38, Kata.dutyFree(700,26,7000));
	}
    public void test_generateShape() {
        assertEquals("+++\n+++\n+++", Kata.generateShape(3));
        assertEquals("+++++\n+++++\n+++++\n+++++\n+++++", Kata.generateShape(5));
        assertEquals("++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++", Kata.generateShape(8));
    }
    public void test_createPhoneNumber()
    {
    	assertEquals("(123) 456-7890", Kata.createPhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}));
    }
    
    public void test_ListJoin() {
    	String[] testinput = {"8", "2", "7", "10"};
    	assertEquals("8,2,7,10", Kata.ListJoin(testinput));
    }
    
    public void test_SumSeries() {
    	assertEquals(6, Kata.SumSeries(4));
    }
    
    public void test_BecomeImmortal() {
    	assertEquals(5, Kata.BecomeImmortal(8,5,1,100));
    	assertEquals(224, Kata.BecomeImmortal(8,8,0,100007));
    	//assertEquals(11925, Kata.BecomeImmortal(25,31,0,100007));
    	//assertEquals(4323, Kata.BecomeImmortal(5,45,3,1000007));
    	//assertEquals(1586, Kata.BecomeImmortal(31,39,7,2345));
    	//assertEquals(808451, Kata.BecomeImmortal(545,435,342,1000007));
    }
   
}
