
TEST(pch, test_test) {
  EXPECT_EQ(1, 1);
  EXPECT_TRUE(true);
}

TEST(pch, test_max) {
	EXPECT_EQ(5, max(5,4));
}

int main(int argc, char** argv) {
	::testing::InitGoogleTest(&argc, argv);

	return RUN_ALL_TESTS();
}
