package Kata

import "testing"
import "strconv"
import "reflect"
//import "strings"
import "fmt"

//import "math/big"

func assertEqual(t *testing.T, a interface{}, b interface{}) {
  if a == b {
    return
    }
    message := fmt.Sprintf("%v != %v", a, b)
    t.Fatal(message)
}


//func formatlist(A []int) {
//    return strings.Trim(strings.Replace(fmt.Sprint(A), " ", ",", -1), "[]")
//}

func TestGetMD5Hash_1(t *testing.T) {
    input := "password"
    expected := "5f4dcc3b5aa765d61d8327deb882cf99"
    actual := GetMD5Hash(input)
    if actual != expected {
        t.Errorf("Test failed! Expected: '%s', got: '%s'", expected, actual)
    }
}

func TestGetMD5Hash_2(t *testing.T) {
    input := "00000"
    expected := "dcddb75469b4b4875094e14561e573d8"
    actual := GetMD5Hash(input)
    if actual != expected {
        t.Errorf("Test failed! Expected: '%s', got: '%s'", expected, actual)
    }
}

func TestBruteMD5Pin_1(t *testing.T) {
    input := "dcddb75469b4b4875094e14561e573d8"
    expected := "00000"
    actual := BruteMD5Pin(input)
    if actual != expected {
        t.Errorf("Test failed! Expected: '%s', got: '%s'", expected, actual)
    }
}

func TestBruteMD5Pin_2(t *testing.T) {
    input := "86aa400b65433b608a9db30070ec60cd"
    expected := "00078"
    actual := BruteMD5Pin(input)
    if actual != expected {
        t.Errorf("Test failed! Expected: '%s', got: '%s'", expected, actual)
    }
}

func TestBruteMD5Pin_3(t *testing.T) {
    input := "827ccb0eea8a706c4c34a16891f84e7b"
    expected := "12345"
    actual := BruteMD5Pin(input)
    if actual != expected {
        t.Errorf("Test failed! Expected: '%s', got: '%s'", expected, actual)
    }
}

func TestBruteMD5Pin_99999(t *testing.T) {
    input := "d3eb9a9233e52948740d7eb8c3062d14"
    expected := "99999"
    actual := BruteMD5Pin(input)
    if actual != expected {
        t.Errorf("Test failed! Expected: '%s', got: '%s'", expected, actual)
    }
}

func Test_reverse_1(t *testing.T) {
    input := "helloworld"
    expected := "dlrowolleh"
    actual := reverse(input)
    if actual != expected {
        t.Errorf("Test failed! Expected: %s, got: %s,", expected, actual)
    }
}


func TestRepeatStr_1(t *testing.T) {
    expected := "aaaa"
    actual := RepeatStr(4, "a") 
    if actual != expected {
        t.Errorf("Test failed! Expected: '%s', got: '%s'", expected, actual)
    }
}
func TestRepeatStr_2(t *testing.T) {
    expected := "abababab"
    actual := RepeatStr(4, "ab") 
    if actual != expected {
        t.Errorf("Test failed! Expected: '%s', got: '%s'", expected, actual)
    }
}

func TestIsDivisible_1(t *testing.T) {
    expected := false
    actual := IsDivisible(3, 3, 4) 
    if actual != expected {
        t.Errorf("Test failed! Expected: '%s', got: '%s'", strconv.FormatBool(expected), strconv.FormatBool(actual))
    }
}

func Test_listrange_1(t *testing.T) {
    expected := []int {0,1,2,3}
    actual := listrange(0,4)
    fmt.Println(reflect.DeepEqual(actual, expected))

    if !reflect.DeepEqual(actual, expected) {
        t.Errorf("list range test failed!")
    //    t.Errorf("Test failed! Expected: '%s', got: '%s'", formatlist(expected), formatlist(actual))
    }
}

func Test_sum_1(t *testing.T){
    expected := 6
    actual := sum(listrange(0,4))
    if actual != expected {
        t.Errorf("Test failed! Expected: '%v', got: '%v'", expected, actual)
    }
}

func Test_BecomeImmortal(t *testing.T){
    expected := 5
    actual := BecomeImmortal(8,5,1,100)
    if actual != expected {
        t.Errorf("Test failed! Expected: '%v', got: '%v'", expected, actual)
    }
}

//func Test_HugeExponent(t *testing.T){
//    number := HugeExponent([]int {12, 30, 21})
//    fmt.Println(number)
//}

func Test_ModExpGoBigInteger(t *testing.T){
    expected := int64(4)
    actual := ModExpGoBigInteger(int64(499942), int64(898102), int64(10))
    if actual != expected {
        t.Errorf("Test failed! Expected: '%v', got: '%v'", expected, actual)
    }
}

func Test_LastDigit(t *testing.T){
    assertEqual(t, 5, LastDigit([]int {5, 20}))
    assertEqual(t, 1, LastDigit([]int {3, 4, 2}))
    assertEqual(t, 6, LastDigit([]int {12, 30, 21}))
    assertEqual(t, 1, LastDigit([]int {7,6,21}))
    assertEqual(t, 6, LastDigit([]int {123232,694022,140249}))
}

//func Test_ToMilliseconds(t *testing.T){
//}