package main

import "fmt"

func Convert (meters float64) float64{
	miles :=  meters * 0.3048
	return miles
}

func main() {
    fmt.Print("Enter a number: ")
    var input float64
    fmt.Scanf("%f", &input)

	output := Convert (input)

    fmt.Println(output)    
}