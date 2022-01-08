package main

import "fmt"

func FindMultiple(number int) int{
	var i int
	var count int
	i = 1
	count = 0
	if number != 0{
		for i <= 100{
			if i % number == 0{
				count++
			}
			i++
		}
	}
	return count
}

func main() {
	x := 3
	output := FindMultiple(x)

    fmt.Println(output)    
}