#include <iostream>
using namespace std;

int main(){
	//User enters integer number
	//Program write out if that number is odd or even
	//cout << 5 % 2 << endl; 
	int number;
	cout << "Please enter whole number: ";
	cin >> number;
	if (number%2 == 0) 
	{
		cout << "Your number is an Even number." << endl;
	}
	else if(number%2 == 1)
	{
		cout << "Your number is an Odd number." << endl;
	}

}