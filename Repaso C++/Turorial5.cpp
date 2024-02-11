#include <iostream>
using namespace std;
int main(){
	//User enters side lengths of a triangle (a,b,c)
	//Program should write out whether tha triangle is
	//equilateral, isoceles or scalene
	float a, b, c;
	cout << "a, b, c:";
	cin >> a >> b >> c;

	if (a == b && b == c)
	{
		cout << "Equilateral triangle";
	}
	else
	{
		if (a != b && a != c && b != c)
		{
			cout << "Scalene triangle";
		}
		else
		{
			cout << "Isoceles triangle";
		}
	}
}