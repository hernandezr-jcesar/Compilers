#include <iostream>
using namespace std;

int main(){
	//Multiplication Table
	int counter;
	for(int i = 1;i <= 2000;i++){
		for(int j = 1; j <= 2000;j++){
			cout << i << " * " << j << " = " << i * j << endl;  
		}
		cout << endl;
	}
	
}