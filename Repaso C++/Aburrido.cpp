#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

struct arbol
{
	int izquierda;
	int derecha;
};

void crear_caso(int casos, int* permutacion);

int main(){
	cout << "" << endl;
	cout << "Este programa transforma una permutacion en un arbol bnario para luego recorrer el arbol\n";
	cout << "y saber en que nivel quedaron cada uno de los elementos de la permutacion dada " << endl;
	int casos;
	cout << "Ingresar cantidad de casos a testear:" << endl;
	cin >> casos;
	int permutacion[casos];

	crear_caso(casos, permutacion);


}

void crear_caso(int casos, int* permutacion){
	srand(time(NULL));
	int tamanio = rand() % 6;

	int *tam  = new int[tamanio];
	

	for(int i = 0; i <= casos; i++){
		for(int j = 0; j <= tamanio; j++){
			*tam[j] = rand() % 10;
		}
	}

}

