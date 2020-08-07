package Kata

import "fmt"
import "crypto/md5"
import "strings"

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

func RepeatStr(repetitions int, value string) string {
    return strings.Repeat(value, repetitions)
}


func IsDivisible(n, x, y int) bool {
    return (n%x==0 && n%y==0)
}
