#include <iostream>
using namespace std;

int main()
{
	//+,-,*,/,%
	cout << 5 + 2 << endl;
	cout << 5 / 2 << endl;
	cout << 5.0 / 2.0 << endl; //2.5
	cout << 5.0 / 2 << endl;  //2.5
	cout << 5 / 2.0 << endl; //2.5
	cout << 5 % 2 << endl; //1

	//++,--
	int counter = 7;
	counter++;
	cout << counter << endl;
	counter--;
	cout << counter << endl;

	system("clear");

	//<,>,<=,>=,==,!=
	int  a = 5, b = 5; // 0 / 1
	cout << (a != b) << endl;

	system("clear");
	// &&,||,!
	int  A = 5, B = 8;
	//cout << (a == 5 && b == 5) << endl;
	cout << (A == 5 && B == 5+3) << endl;

	system("clear");
	//=,+=,-=,*=,/=,%=
	int x = 5;
	x += 7;
	//x = x + 7;
	cout << x << endl;



}