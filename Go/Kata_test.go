package Kata

import "testing"
import "strconv"
import "reflect"
//import "strings"
import "fmt"

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
    //actual := []int {1,2,3,4}
    actual := listrange(0,4)
    fmt.Println(reflect.DeepEqual(actual, expected))

    if !reflect.DeepEqual(actual, expected) {
    //if true {
        t.Errorf("list range test failed!")
    //    t.Errorf("Test failed! Expected: '%s', got: '%s'", formatlist(expected), formatlist(actual))
    }
}


