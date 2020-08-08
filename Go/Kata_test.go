package Kata

import "testing"
//import "strconv"
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
func assertDeepEqual(t *testing.T, a interface{}, b interface{}) {
  if reflect.DeepEqual(a, b) {
    return
    }
    message := fmt.Sprintf("%v != %v", a, b)
    t.Fatal(message)
}

func Test_GetMD5Hash(t *testing.T) {
    assertEqual(t, "5f4dcc3b5aa765d61d8327deb882cf99", GetMD5Hash("password"))
    assertEqual(t, "dcddb75469b4b4875094e14561e573d8", GetMD5Hash("00000"))
}

func Test_BruteMD5Pin(t *testing.T) {
    assertEqual(t, "00000", BruteMD5Pin("dcddb75469b4b4875094e14561e573d8"))
    assertEqual(t, "00078", BruteMD5Pin("86aa400b65433b608a9db30070ec60cd"))
    assertEqual(t, "12345", BruteMD5Pin("827ccb0eea8a706c4c34a16891f84e7b"))
    assertEqual(t, "99999", BruteMD5Pin("d3eb9a9233e52948740d7eb8c3062d14"))
    assertEqual(t, "99999", BruteMD5Pin("d3eb9a9233e52948740d7eb8c3062d14"))
}

func Test_reverse(t *testing.T) {
    assertEqual(t, "dlrowolleh", reverse("helloworld"))
}

func Test_RepeatStr(t *testing.T) {
    assertEqual(t, "aaaa", RepeatStr(4, "a"))
    assertEqual(t, "abababab", RepeatStr(4, "ab"))
}

func Test_IsDivisible(t *testing.T) {
    assertEqual(t, false, IsDivisible(3, 3, 4))
}

func Test_listrange(t *testing.T) {
    assertDeepEqual(t, []int {0,1,2,3}, listrange(0,4))
}

func Test_sum(t *testing.T){
    assertEqual(t, 6, sum(listrange(0,4)))
}

func Test_BecomeImmortal(t *testing.T){
    assertEqual(t, 5, BecomeImmortal(8,5,1,100))
}

//func Test_HugeExponent(t *testing.T){
//    number := HugeExponent([]int {12, 30, 21})
//    fmt.Println(number)
//}

func Test_ModExpGoBigInteger(t *testing.T){
    assertEqual(t, int64(4), ModExpGoBigInteger(int64(499942), int64(898102), int64(10)))
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