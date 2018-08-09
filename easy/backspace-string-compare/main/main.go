/*
	A simple main package to make sure that we can call functions from
	backspaceCompare package.
*/

package main

import (
	"fmt"
	"leetcode/backspace-string-compare/backspaceCompare"
)

func main() {
	fmt.Println("ab#c and ad#c:\n", backspaceCompare.BackspaceCompare("ab#c", "ad#c"), "\n")
	fmt.Println("ab## and c#d#:\n", backspaceCompare.BackspaceCompare("ab##", "c#d#"), "\n")
	fmt.Println("a##c and #a#c:\n", backspaceCompare.BackspaceCompare("a##c", "#a#c"), "\n")
	fmt.Println("a#c and b:\n", backspaceCompare.BackspaceCompare("a#c", "b"), "\n")

}
