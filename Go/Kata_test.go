package Kata

import "testing"

func GetMD5Hash_test1(t *testing.T) {
	input := "password"
	expected := "5f4dcc3b5aa765d61d8327deb882cf99"
	actual := GetMD5Hash(input)
	if actual != expected {
		t.Errorf("Test failed! Expected: '%s', got: '%s'", expected, actual)
	}
}

func RepeatStr_test1(t *testing.T) {
	expected := "aaaa"
	actual := RepeatStr(4, "a") 
	if actual != expected {
		t.Errorf("Test failed! Expected: '%s', got: '%s'", expected, actual)
	}
}

