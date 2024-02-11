#include <iostream>
using namespace std;

int main(){
	/*
	cout << (int)'a' << endl;
	cout << int('a') << endl;
	cout << int('A') << endl;
	cout << char(65) << endl;
	*/
	char c1, c2, c3, c4, c5;
	cout << "Enter 5 letters: ";
	cin >> c1 >> c2 >> c3 >> c4 >> c5;
	cout << "ASCII message: " << int(c1) << " " << int(c2)
	 << " " << int(c3) << " " << int(c4) << " " << int(c5) << endl;

	cout << "Mensaje en ingles" << endl;
	cout << "English message: " << char(int(c1)) << "" << char(int(c2))
	 << "" << char(int(c3)) << "" << char(int(c4)) << "" << char(int(c5));
}