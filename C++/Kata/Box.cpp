//
//
//

class Box {
public:
    Box(double width, double height, double length)
    {
        this->width = width;
        this->height = height;
        this->length = length;
    }

    double getVolume(void) {
        return this->width * this->height * this->length;
    }
    void setWidth(double width) {
        this->width = width;
    }
    void setHeight(double height) {
        this->height = height;
    }
    void setLength(double length) {
        this->length = length;
    }
private:
    double width;
    double height;
    double length;
};

TEST(pch, test_Box1) {
    Box Box1(6.0, 7.0, 5.0);
	EXPECT_EQ(210, Box1.getVolume());
}
