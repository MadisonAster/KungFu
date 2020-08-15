//
//
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
