import java.util.*;
public class Linea{
	private ArrayList<String> elementos = new ArrayList<String>();	//cada línea cuenta con un n número de elementos
	private int numelementos;
	//constructores
	public Linea(String fileline){
		String[] temp1=fileline.split(",");		//separar la línea cada que se encuentre una coma
		for (int i=0;i<temp1.length;i++) {
			temp1[i]=temp1[i].strip();			//eliminar espacios en blanco
		}
		Collections.addAll(elementos,temp1);	//guardar cada elemento en el arraylist
		numelementos=elementos.size();			//obtener número de elementos
	}

	public Linea(String estado, String simbolo, String nuevoestado){	//constructor para linea que se agregará al set de transiciones
		elementos.add(estado);
		elementos.add(simbolo);
		elementos.add(nuevoestado);
		numelementos=elementos.size();
	}

	//métodos

	public void imprimir(){						//imprime el número de elementos y lo que contiene el arraylist
		System.out.println(numelementos);
		System.out.println(elementos);
	}
	
	public String toString(){					//regresa los elementos del arraylist en String
		return ""+elementos;
	}

	public void addEE(){ //añadir estado de error (para states)		*no se ocupó*
		elementos.add("EE");
		numelementos++;
	}

	public int howmany(){	//regresa el número de elementos
		return numelementos;
	}

	public String singleelement(int ind){	//regresa un solo elemento del arraylist elementos, siendo ind el índice
		return (elementos.get(ind));
	}

	public ArrayList<String> dameelarraywe(){	//regresa todo el arraylist "elementos"
		return elementos;
	}
}