#include <iostream>
using namespace std;

int main()
{
	//Programa para cambiar valores de dos variables
	int a = 20;
	int b = 10;
	/*
	int temp = a;
	a = b;
	b = temp;
	*/
	a = a + b;//30
	b = a - b;//20
	a = a - b;//10
	cout << "a =" << a << ", b =" << b << endl;

}