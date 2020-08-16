double SakuraFall(double v) {
	if (v > 0) {
		return 400 / v;
	}
	else {
		return 0;
	};
}
TEST(pch, test_SakuraFall) {
	EXPECT_EQ(80, SakuraFall(5));
}