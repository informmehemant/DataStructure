package main

import( "fmt" )



// Function to left rotate arr[] once  
func leftRotatebyOne(arr []int,  n int) {
	var temp, i int

	temp = arr[0]

	for i = 0; i<n-1; i++ {
		arr[i] = arr[i + 1]
	}
	arr[i] = temp
	
}

//  Function that rotates the array by n times
func leftRotatebyNtimes(arr []int, d int, n int) {
	
	for i := 0; i<d; i++ {
	   leftRotatebyOne(arr, n)		
	} 
	
}
func main() {
	
	fmt.Println("Rotation of array \n")

	arr := []int {1,2,3,4,5,6,7}
	
	leftRotatebyNtimes(arr, 2, 7)

}