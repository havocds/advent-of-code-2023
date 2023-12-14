package main

import (
	"fmt"
	"os"
	"log"
	"reflect"
	
)
func main() {
	lines, err := os.ReadFile("../test_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(lines), err)
	fmt.Println(reflect.TypeOf(lines))

	for index, c := range lines {
		fmt.Println(index, string(c))
	}
}