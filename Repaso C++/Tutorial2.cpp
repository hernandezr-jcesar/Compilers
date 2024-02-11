#include <iostream>
#include <climits>
using namespace std;

int main(){
	/*
	float salarioanual;
	cout << "¿Cual es tu salario mensual?";
	cin >> salarioanual;
	float salariomensual = 	salarioanual / 12;
	cout << "Tu salario mensual es: " << salariomensual;
	cout << "\nEn 10 años ganaras: " << salarioanual * 10 ;
	char caracter = 'a';
	*/
	/*
	int yearthOfBirth = 2001;
	char genero = 'm';
	bool esmayorque18 = true;
	float averageGrade = 4.5;
	double balance = 45678945856;

	cout << "Size of int is " << sizeof(int) << "bytes\n";
	//-1,-2,-3,...,-2147483648(2³²)
	cout << "El valor minimo de int es: " << INT_MIN << endl;
	//0,+1,+2,+3,...,+214748364
	cout << "El valor maximo de int es: " << INT_MAX << endl;

	cout << "Tamanio de unsigned Int" << sizeof(unsigned int) << "bytes\n";
	cout << "unsigned int max value is: " << UINT_MAX << endl;

	cout << "Size of bool is " << sizeof(bool) << " bytes\n";
	cout << "Size of char is " << sizeof(char) << " bytes\n";
	cout << "Size of float is " << sizeof(float) << " bytes\n";
	cout << "Size of double is " << sizeof(double) << " bytes\n";
	*/
	//Data Type Overflow
	int intMax = INT_MAX;
	cout << INT_MAX << endl;
	cput << INT_MAX + 1;
}