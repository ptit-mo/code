package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Cho hai số N, K và một tập con K phần tử X[] =(X1, X2,.., XK) của 1, 2, .., N. Nhiệm vụ của bạn là hãy đưa ra tập con K phần tử trước đó của X[]. Ví dụ N=5, K=3, X[] ={2, 3, 5} thì tập con trước đó của X[] là {2, 3, 4}. Chú ý nếu tập con trong input là đầu tiên thì trước đó là tập con cuối cùng.
// Input:
// Dòng đầu tiên đưa vào số lượng test T.
// Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test gồm hai dòng: dòng thứ nhất
// là hai số N và K; dòng tiếp theo đưa vào K phần tử của X[] là một tập con K
// phần tử của 1, 2, .., N.
// T, K, N, X[] thỏa mãn ràng buộc: 1≤T≤100; 1≤K≤N≤103.
// Output:
// Đưa ra kết quả mỗi test theo từng dòng.
// Ví dụ:
// Input
// 2
// 5  3
// 2  3  5
// 5  3
// 1  2  3
// Output
// 2 3 4
// 3 4 5

func main() {
	tests := inputNum()
	scanner := bufio.NewScanner(os.Stdin)
	for i := 0; i < tests; i++ {
		biggest := inputArrNum(scanner)[0]
		arr := inputArrNum(scanner)
		findPrevPerm(arr, biggest)
	}
}

func findPrevPerm(target []int, biggest int) {
	found := 0
	ln := len(target)
	var prev, res []int
	var backtrack func (cur []int, head int) 
	backtrack = func (cur []int, head int)  {
		if len(cur) == ln {
			if found == 1 {
				found++
			}
			if arrEqual(cur, target) {
				res = prev
				found = 1
			}
			prev = cur
			return
		}
		for i := head; i <= biggest; i++ {
			backtrack(append(cur, i), i+1)
			if found > 1 {
				break
			}
		} 
	}
	backtrack([]int{}, 1)
	if res == nil {
		for i := biggest - ln; i< biggest; i++ {
			res = append(res, i+1)
		}
	}
	fmt.Print(strings.Join(arrNumToArrString(res), " "))
}

func arrNumToArrString(arr []int) []string {
	res := make([]string, 0, len(arr))
	for _, num := range arr {
		res = append(res, strconv.Itoa(num))
	}
	return res
}

func arrEqual(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func inputNum() int {
	var num int
	fmt.Scan(&num)
	return num
}

func inputArrNum(scanner *bufio.Scanner) []int {
	scanner.Scan()
	line := scanner.Text()
	numSs := strings.Split(line, " ")
	nums := make([]int, 0, len(numSs))
	for _, str := range numSs {
		num , _ := strconv.Atoi(str)
		nums = append(nums, num)
	}
	return nums
}