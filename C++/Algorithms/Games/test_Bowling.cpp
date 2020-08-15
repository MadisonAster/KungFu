
TEST(pch, test_GameOfBowling) {
	EXPECT_EQ(5, GameOfBowling(5));
}

int main2(int argc, char** argv) {
	::testing::InitGoogleTest(&argc, argv);

	return RUN_ALL_TESTS();
}
