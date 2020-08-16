//
//General Math
//

int max(int a, int b) {
	int result;
	if (a > b)
		result = a;
	else
		result = b;
	return result;
}
TEST(pch, test_max) {
	EXPECT_EQ(5, max(5, 4));
}


bool isDivisible(int n, int x, int y) {
	return n % x == 0 && n % y == 0;
}
TEST(pch, test_isDivisible1) {
	EXPECT_EQ(false, isDivisible(3, 3, 4));
}
TEST(pch, test_isDivisible2) {
	EXPECT_EQ(true, isDivisible(12, 3, 4));
}
