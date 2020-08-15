//
// pch.cpp
// Include the standard header and generate the precompiled header.
//

#include "pch.h"
#include <iostream>

int max(int a, int b) {
	int result;
	if (a > b)
		result = a;
	else
		result = b;
	return result;
}
