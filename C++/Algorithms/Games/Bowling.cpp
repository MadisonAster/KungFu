//
//
//

#include "gtest/gtest.h"



int GameOfBowling(int a) {
	return a;
}

TEST(pch, test_GameOfBowling) {
	EXPECT_EQ(5, GameOfBowling(5));
}