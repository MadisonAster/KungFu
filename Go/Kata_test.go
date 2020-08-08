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

func Test_ToMilliseconds(t *testing.T){
    assertEqual(t, 61000, ToMilliseconds(0, 1, 1))
    assertEqual(t, 3661000, ToMilliseconds(1, 1, 1))
    assertEqual(t, 0, ToMilliseconds(0, 0, 0))
    assertEqual(t, 3601000, ToMilliseconds(1, 0, 1))
    assertEqual(t, 3600000, ToMilliseconds(1, 0, 0))
}

func Test_ExpressionsMatter(t *testing.T){
    assertEqual(t, 6, ExpressionsMatter(2, 1, 2))
    assertEqual(t, 4, ExpressionsMatter(2, 1, 1))
    assertEqual(t, 3, ExpressionsMatter(1, 1, 1))
    assertEqual(t, 9, ExpressionsMatter(1, 2, 3))
    assertEqual(t, 5, ExpressionsMatter(1, 3, 1))
    assertEqual(t, 8, ExpressionsMatter(2, 2, 2))
    assertEqual(t, 20, ExpressionsMatter(5, 1, 3))
    assertEqual(t, 105, ExpressionsMatter(3, 5, 7))
    assertEqual(t, 35, ExpressionsMatter(5, 6, 1))
    assertEqual(t, 8, ExpressionsMatter(1, 6, 1))
    assertEqual(t, 14, ExpressionsMatter(2, 6, 1))
    assertEqual(t, 48, ExpressionsMatter(6, 7, 1))
    assertEqual(t, 60, ExpressionsMatter(2, 10, 3))
    assertEqual(t, 27, ExpressionsMatter(1, 8, 3))
    assertEqual(t, 126, ExpressionsMatter(9, 7, 2))
    assertEqual(t, 20, ExpressionsMatter(1, 1, 10))
    assertEqual(t, 18, ExpressionsMatter(9, 1, 1))
    assertEqual(t, 300, ExpressionsMatter(10, 5, 6))
    assertEqual(t, 12, ExpressionsMatter(1, 10, 1))
}

func Test_DirReduc(t *testing.T){
    assertDeepEqual(t, []string{"NORTH"}, DirReduc([]string{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"}))
    assertDeepEqual(t, []string{"NORTH", "WEST", "SOUTH", "EAST"}, DirReduc([]string{"NORTH", "WEST", "SOUTH", "EAST"}))
    assertDeepEqual(t, []string{"WEST"}, DirReduc([]string{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"}))
    assertDeepEqual(t, []string{}, DirReduc([]string{"NORTH", "SOUTH", "EAST", "WEST"}))
}
