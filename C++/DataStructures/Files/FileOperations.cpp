#include <iostream>
#include <fstream>
#include <istream>
#include <string>
//using namespace std;

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


	//std::string text = in.get();
	//return text;

	//getline(in, line)
	
	//in >> num >> str;

	//if (in.fail())
	//	in.clear();
}

/*
void WriteFileText(std::string fpath, std::string ftext) {
	ofstream out;
	out.open(fpath.c_str());
	out.put(ftext);
	//out << num << str;
}
*/

//void WriteFileLines(std::string fpath, std::array<std::string>& lines) {
//	//out << line << endl;
//}



TEST(pch, test_WriteRead1) {
	std::string ftext = "0123456789";
	std::string fpath = ""; //tempfile somehow?
	//WriteFileText(fpath, ftext);
	//string rtext = ReadFileText(fpath);
	//EXPECT_EQ(rtext, ftext);
}

