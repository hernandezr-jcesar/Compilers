#include <iostream>
using namespace std;

//Es una forma en la que ya no se tiene que 
//repetir codigo inescesario usando genericos
//el cual es un tipo de dato generico que
//puede tomar el tipo dependiendo de las entradas
template<typename T>

void Swap(T& a, T& b){
	T temp = a;
	a = b ;
	b = temp;
}
int main(){
	int a = 5, b = 7; 
	cout << a << " - " << b << endl;
	Swap(a, b);
	cout << a << " - " << b << endl;

	char c = 'c', d = 'd';
	cout << c << " - " << d << endl;
	Swap(c, d);
	cout << c << " - " << d << endl;
}
