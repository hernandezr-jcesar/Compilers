#include <iostream>
using namespace std;

int main(){
	//The factorial of a number
	//6!=1*2*3*4*5*6=720

	int number;
	cout << "Number: ";
	cin >> number;//3
	int factorial = 1;
	/*
	for(int i = 1;i <= number;i++){
		factorial = factorial * i;
	}
	*/
	//6!=1*2*3*4*5*6=720	
	for(int i = number; i >= 1; i--){
		factorial = factorial *i;
	}
	cout << number << "!=" << factorial;
	cout << "" << endl;
}