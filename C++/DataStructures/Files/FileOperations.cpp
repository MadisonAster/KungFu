#include <iostream>
#include <fstream>
#include <istream>
#include <string>


#include <cstdio>
#include <cstdlib>
#include <filesystem>
//#include <boost/filesystem.hpp>

//using namespace std;


//namespace fs = std::filesystem;

/*
void ReadFileLines() {

}

void GetLines(std::ifstream& in) {
	int count = 0;
	while (true) {
		std::string line;
		std::getline(in, line);
		if (in.fail()) {
			in.clear();
			break;
		}
		count++;
	}
}


int CountLines(std::ifstream& in) {
	int count = 0;
	while (true) {
		std::string line;
		std::getline(in, line);
		if (in.fail()) {
			in.clear();
			break;
		}
		count++;
	}
	return count;
}
*/

std::string ReadFileText(std::string fpath) {
	std::ifstream in;
	in.open(fpath.c_str());

	if (in)
	{
		std::string contents;
		in.seekg(0, std::ios::end);
		contents.resize(in.tellg());
		in.seekg(0, std::ios::beg);
		in.read(&contents[0], contents.size());
		in.close();
		return(contents);
	}
	throw(errno);
	//getline(in, line)
}


void WriteFileText(std::string fpath, std::string ftext) {
	std::ofstream out;
	out.open(fpath.c_str());

	char* cstr = new char[ftext.length() + 1];
	std::strcpy(cstr, ftext.c_str());

	out.put(*cstr);
	//out << num << str;
}


std::string GetTempFilePath() {
	char name[L_tmpnam];
	return std::tmpnam(name);
	//std::FILE* tmpf = std::tmpfile();
	//std::fputs(ftext.c_str(), tmpf);
}

TEST(pch, test_WriteRead1) {
	std::string ftext = "0123456789";
	std::string fpath = GetTempFilePath();
	WriteFileText(fpath, ftext);

	std::string rtext = ReadFileText(fpath);
	EXPECT_EQ(rtext, ftext);
}

