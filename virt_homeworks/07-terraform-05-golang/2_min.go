package main
    
import "fmt"

func FindMin(array []int) int{
	min := array[0]
	for _, value := range array{
		if value < min{
			min = value
		}
	}
	return min
}

func main() {
    x := []int{48,96,86,68,57,82,63,70,37,34,83,27,19,97,9,17,}
	output := FindMin(x)
	fmt.Println(output)    
}