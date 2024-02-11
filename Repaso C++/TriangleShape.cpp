#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	int lenght;
	cout << "Lenght: ";
	cin >> lenght;
	char symbol;
	cout << "Symbol: ";
	cin >> symbol;

	for(int i = 1; i <= lenght; i++){
		for(int j = 1; j <= i; j++){
			cout << setw(2) << symbol;
		}
		cout << endl;
	}
	cout << endl << endl; 

	for(int i = lenght; i >= 1; i--){
		for(int j = 1; j <= i; j++){
			cout << setw(2) << symbol;
		}
		cout << endl;
	}

}