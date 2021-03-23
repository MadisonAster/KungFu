#include "gtest/gtest.h"

std::string PlanetById(int id)
{
	switch (id)
	{
	case 1:
		return "Mercury";
		break;
	case 2:
		return "Venus";
		break;
	case 3:
		return "Earth";
		break;
	case 4:
		return "Mars";
		break;
	case 5:
		return "Jupiter";
		break;
	case 6:
		return "Saturn";
		break;
	case 7:
		return "Uranus";
		break;
	case 8:
		return "Neptune";
		break;
	default:
		throw new std::exception();
	};
};

TEST(pch, test_GetPlanet3) {
	EXPECT_EQ("Earth", PlanetById(3));
}

TEST(pch, test_GetPlanet8) {
	EXPECT_EQ("Neptune", PlanetById(8));
}
