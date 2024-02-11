#include <iostream>
using namespace std;

/*
void introduceMe(string name, string city, int age=0){
	cout << "My name is " << name << endl;
	cout << "I am from " << city << endl;
	if(age != 0){
	cout << "I am " << age << " years old" << endl;
	}
}
*/
bool isPrimeNumber(int number){
	bool isPrimeFlag=true;
	for (int i = 2; i < number; i++) {
		if (number % i == 0) { 
			return false;
		}
	}
	return true;
}
int main(){
	for (int i =1; i <= 1000; i++){
		bool isPrime = isPrimeNumber(i);
		if (isPrime){
			cout << i << " is prime number\n";
		}
	}
	/*
	introduceMe("Julio", "Mexico", 20);
	introduceMe("Cesar", "USA");
	
	string name, city;
	int age;
	cout << "Name: ";
	cin >> name;
	cout << "City: ";
	cin >> city;
	cout << "Age: ";
	cin >> age;
	introduceMe(name, city, age);
	*/
	
	/*
	int number;
	cout << "Number: ";
	cin >> number;
	/*
	bool isPrimeFlag=true;
	for (int i = 2; i < number; i++) {
		if (number % i == 0) { 
			isPrimeFlag = false;
			break;
		}
	}
	
	bool isPrimeFlag=isPrimeNumber(number);

	if (isPrimeFlag){
		cout << "Prime number" << endl;
	}else{
		cout << "Not prime number" << endl;
	}
	*/
}
