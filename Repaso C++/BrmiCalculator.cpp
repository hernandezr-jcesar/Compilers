#include <iostream>
using namespace std;

int main()
{
	/*
	BMI calculator
	peso(kg) / altura * altura(m)
	sobrepeso > 25
	Peso normal 18.5 - 24.9
	Underweight < 18.5 
	*/
	float peso, altura, bmi;
	cout << "Peso(kg), Altura(m):";
	cin >> peso >> altura;
	bmi = peso / (altura * altura);

	if (bmi < 18.5){
		cout << "Underweight" << endl;
	}
	else if(bmi > 25){
		cout << "Sobrepeso" << endl;
	}
	else{
		cout << "Peso Normal" << endl;
	}
	cout << "Tu bmi es de: " << bmi;
}
