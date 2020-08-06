import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Kata_tests {
	@Test
	void test_square() {
	assertEquals(25, Kata.square(5));
	}
	
	@Test
	void test_fakeBin1() {
		assertEquals("1100", Kata.fakeBin("6644"));
	}
	
	@Test
	void dutyFree_test() {
		System.out.println(System.getProperty("java.vm.version"));
	    assertEquals(166, Kata.dutyFree(12,50,1000));
	    assertEquals(294, Kata.dutyFree(17,10,500));
	    assertEquals(357, Kata.dutyFree(24,35,3000));
	    assertEquals(20, Kata.dutyFree(1400,35,10000));
	    assertEquals(38, Kata.dutyFree(700,26,7000));
	}

	@Test
    public void generateShape_test() {
        assertEquals("+++\n+++\n+++", Kata.generateShape(3));
        assertEquals("+++++\n+++++\n+++++\n+++++\n+++++", Kata.generateShape(5));
        assertEquals("++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++", Kata.generateShape(8));
    }
	
	@Test
	public void createPhoneNumber_test() {
	    assertEquals("(123) 456-7890", Kata.createPhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}));
	}

}
