package Kata

import "fmt"
import "crypto/md5"
import "strings"
import "math/big"
import "strconv"

func main() {
    fmt.Println("hello world")
    fmt.Println("go" + "lang")

    fmt.Println("1+1 =", 1+1)
    fmt.Println("7.0/3.0 =", 7.0/3.0)

    //var a = "initial"
    var b int = 100
    fmt.Println(b)


    var twoD [2][3]int
    for i := 0; i < 2; i++ {
        for j := 0; j < 3; j++ {
            twoD[i][j] = i + j
        }
        break
    }
    fmt.Println(twoD)
}

func GetMD5Hash(str string) string {
    return fmt.Sprintf("%x",md5.Sum([]byte(str)))
}

func BruteMD5Pin(hash string) (result string) {
    for i := 0; i <= 99999; i++ {
        if hash == fmt.Sprintf("%x",md5.Sum([]byte(fmt.Sprintf("%05d", i)))) {
            result = fmt.Sprintf("%05d", i)
            break
        }
    }
    return
}

func RepeatStr(repetitions int, value string) string {
    return strings.Repeat(value, repetitions)
}

func reverse(s string) (result string) {
    for _, v := range s {
        result = string(v) + result
    }
    return
}

func IsDivisible(n, x, y int) bool {
    return (n%x==0 && n%y==0)
}

func listrange(start, end int) []int {
    s := make([]int, end-start)
    for i := range s {
        s[i] = i
    }
    return s
}

func sum(array []int) int {
    result := 0
    for _, v := range array {
        result += v
    }
    return result
}

func BecomeImmortal(m int, n int, l int, t int) int {
    rowvalue := sum(listrange(0,m))
    rowsubtract := l*(m-1)
    row := rowvalue - rowsubtract
    total := row * n
    return total % 100
}

//func HugeNumber(x int64, y int64) *big.Int{
func HugeExponent(A []int) *big.Int{
    exponent := big.NewInt(int64(A[0]))
    //fmt.Println(exponent)
    for i := 1; i < len(A); i++ {
        exponent = new(big.Int).Exp(exponent, big.NewInt(int64(A[i])), nil)
        //fmt.Println(exponent)
    }
    //result := new(big.Int).Exp(big.NewInt(x), big.NewInt(y), nil)
    return exponent
}

func LastDigit1(as []int) int {
    exponent := big.NewInt(int64(as[0]))
    for i := 1; i < len(as); i++ {
        exponent = new(big.Int).Exp(exponent, big.NewInt(int64(as[i])), nil)
    }
    Sexponent := exponent.String()
    newresult := Sexponent[len(Sexponent)-1:]
    result, _ := strconv.Atoi(newresult)
    return result
}

func ModExpGoBigInteger(base, exponent, modulus int64) int64 {
    return new(big.Int).Mod(new(big.Int).Exp(big.NewInt(base), big.NewInt(exponent), nil), big.NewInt(modulus)).Int64()
}

func ModExpGoBigIntegerExp(base, exponent, modulus int64) int64 {
    return new(big.Int).Exp(big.NewInt(base), big.NewInt(exponent), big.NewInt(modulus)).Int64()
}

func LastDigit2(as []int) int {
    exponent := int64(as[0])
    for i := 1; i < len(as); i++ {
        exponent = ModExpGoBigIntegerExp(exponent, int64(as[i]), int64(10))
        fmt.Println(exponent)
    }
    fmt.Println("---")
    fmt.Println(exponent)
    Sexponent := strconv.FormatInt(exponent, 10)
    newresult := Sexponent[len(Sexponent)-1:]
    result, _ := strconv.Atoi(newresult)
    return result
}

func LastDigit(as []int) int {
    exponent := int64(as[len(as)-1])
    for i := len(as)-2; i >= 0; i-- {
        exponent = ModExpGoBigIntegerExp(int64(as[i]), exponent, int64(100))
        fmt.Println(exponent)
    }
    fmt.Println("---")
    fmt.Println(exponent)
    Sexponent := strconv.FormatInt(exponent, 10)
    newresult := Sexponent[len(Sexponent)-1:]
    result, _ := strconv.Atoi(newresult)
    return result
}
