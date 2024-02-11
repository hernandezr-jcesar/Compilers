#include <iostream>
using namespace std;

int main(){

	int hostUserNum, guestUserNum;
	cout << "Host: ";
	cin >> hostUserNum;
	system("clear");
	cout << "Guest: ";
	cin >> guestUserNum;
	/*
	if(hostUserNum == guestUserNum){
		cout << "Correct!";
	}else{
		cout << "Failed!";
	}
	*/
	//NUEVA FORMA DE USAR IF ELSE reducido con una preguna ternaria
	// (Condicion) ? (Hacer esto si la condicion es verdadera) : (HAcer esto si la condicion es falsa)
	(hostUserNum == guestUserNum)? cout << "Correct!" : cout << "Failed!";
}