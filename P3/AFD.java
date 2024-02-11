import java.util.*;
public class AFD{
	private ArrayList<String> finalstates = new ArrayList<String>();	//descomentar si es necesario indicar cuáles serían inciales y finales
	private String initialstate;		//descomentar si es necesario indicar cuáles serían inciales y finales
	private ArrayList<String> alphabet;
	private ArrayList<Big_State> bstates = new ArrayList<Big_State>();	//estados del afd
	private ArrayList<String> temp = new ArrayList<String>();	//arraylist<string> auxiliar, para ir guardando las C_E
	private char chia='A';		//Para ir nombrando los estados del afd
	private Transition set = new Transition();	//set de transiciones del afd

	//constructores
	public AFD(ArrayList<String> og_alphabet){		//crear el afd, e inicializarlo copiando el alfabeto del otro automata a este
		alphabet = new ArrayList<String>(og_alphabet);
		Collections.sort(alphabet);		//ordenar el alfabeto
	}

	//métodos
	public void crear(Linea og_states, Linea og_finalstates, String og_initialstate, Transition og_set){	//construir todo el afd
		temp.add(og_initialstate);
		this.C_E(og_initialstate, og_set);	//generar cerradura epsilon de q0, se guarda en temp
		//System.out.println("C_E("+og_initialstate+") = "+temp);	//prueba
		String aux_chia=Character.toString(chia);	//"A", le puedes ir sumando :0
		Big_State bs_temp = new Big_State(aux_chia, temp);	//crear el big state "A", que resulta de la C_E(q0)
		bstates.add(bs_temp);	//añadir el bigstate previamente creado a la lista que contendrá todos los big states
		initialstate=aux_chia;
		temp.clear();
		for (int i=0; i < bstates.size() ; i++ ) {		//con cada Big_State hace la operación Ir_A con cada elemento del alfabeto
			for (int j=0; j<alphabet.size(); j++) {
				this.Ir_A(bstates.get(i), alphabet.get(j), og_set);
			}
		}
		this.cualesfinales(og_finalstates);
	}

	public void C_E(String state,Transition og_set){
		//a intentarlo con epsilon E perrooo
		String actual=state;
		for (int j=0; j<og_set.CuantasRows(); j++) {	//este for recorre las rows del set de transición
			if ((!(temp.contains(og_set.singleelement_of_a_row(j,2))))&&(actual.equals(og_set.singleelement_of_a_row(j,0)))&&(og_set.singleelement_of_a_row(j,1).equals("E"))) {	//checa si el estado actual cuenta con alguna transición epsilon E
				actual=og_set.singleelement_of_a_row(j,2);		//ahora nuestro estado actual será el estado siguiente, que nos lo da la row de la función de transición
				temp.add(actual);					//añadir dicho estado al arraylist que va guardando el camino
				this.C_E(actual, og_set);
				actual=state;
			}
		}
		Collections.sort(temp);
	}

	public void Ir_A(Big_State statee, String symbol, Transition og_set){
		temp.clear();
		ArrayList<String> MoverResult = new ArrayList<String>(this.Mover(statee, symbol, og_set));	//En MoverResult se almacena el arraylist de estados resultantes de la operación mover(BS, symbol)
		for (String okok : MoverResult) {	//para cada estado resultante de mover, sacar C_E
			temp.add(okok);
			this.C_E(okok, og_set);
		}
		//terminando el for anterior, en temp se alojará el resultado de C_E(Mover(bigstate,symbol))
		//System.out.println("C_E("+MoverResult+") = "+temp);	//prueba
		//System.out.println("Ir_A("+statee.getID()+","+symbol+") = "+temp);	//prueba

		//checar si temp is Empty, if true, EE

		if (temp.isEmpty()) {
			Linea templine = new Linea(statee.getID(), symbol, "//");
			set.addLine(templine);
			//System.out.println("Nueva transición creada: "+templine);	//prueba
		}
		else{
			//ahora a checar si ya existe el bigstate, y añadir transición al set
			String siguiente;	//
			boolean ya_existe=false;
			for (Big_State okok: bstates) {	//recorre los estados del afd
				if (temp.equals(okok.dameelarraywe())) {	//checa si ya existe algun bstate que contenga en sus ministates lo mismo que está en temp
					ya_existe=true;		//confirma que ya existe un bstate que cumple la condición anterior
					siguiente=okok.getID();
					Linea templine = new Linea(statee.getID(), symbol, siguiente);	//crear nueva transición, con el bstate og, el simbolo y pal siguiente
					set.addLine(templine);	//añade la transición al set
					//System.out.println("Nueva transición creada: "+templine);	//prueba
				}
			}
			if (!(ya_existe)) {	//si no existía ya un bstate que cumplía con dat
				chia++;		//para el id del big state (A+1=B)
				String aux_chia=Character.toString(chia);	//*****"A", le puedes ir sumando :0
				Big_State bs_temp = new Big_State(aux_chia, temp);	//crear bstate id="X", y temp= ministates
				bstates.add(bs_temp);	//añadir el bigstate previamente creado a la lista que contendrá todos los big states
				//System.out.println("Se ha creado un nuevo Big_State: "+bs_temp);	//prueba
				temp.clear();
				//lo siguiente crea la transición y la añade al set
				siguiente=aux_chia;
				Linea templine = new Linea(statee.getID(), symbol, siguiente);
				set.addLine(templine);
				//System.out.println("Nueva transición creada: "+templine);	//prueba
			}
		}
	}

	public ArrayList<String> Mover(Big_State statee, String symbol, Transition og_set){
		ArrayList<String> result = new ArrayList<String>();
		for (String okok : statee.dameelarraywe()) {			//recorre los mini states que contiene el big state
			for (int j=0; j<og_set.CuantasRows(); j++ ) {		//este for recorre las rows del set de transición
				if ((okok.equals(og_set.singleelement_of_a_row(j,0)))&&(symbol.equals(og_set.singleelement_of_a_row(j,1)))/*&&(!(og_set.singleelement_of_a_row(j,2).equals("EE")))*/) {	//si necesitas usar .completar (EE), descomenta
					result.add(og_set.singleelement_of_a_row(j,2));
				}
			}
		}
		Collections.sort(result);
		//System.out.println("Mover("+statee.getID()+","+symbol+") = "+result);	//prueba
		return result;
	}

	public void imprimirTabla(){
		Collections.sort(alphabet);
		System.out.print("-");
		for (String okok : alphabet) {
			System.out.print("\t|\t"+okok);
		}
		//System.out.println();
		for (Big_State okok: bstates) {
			String tempstate=okok.getID();
			System.out.print("\n"+tempstate);
			for (int j=0; j<set.CuantasRows(); j++) {	//este for recorre las rows del set de transiciones
				if (tempstate.equals(set.singleelement_of_a_row(j,0))) {
					System.out.print("\t|\t"+set.singleelement_of_a_row(j,2));
				}
			}
		}
		System.out.println("\nEstado Inicial: "+initialstate);
		System.out.println("Estados Finales: "+finalstates);
	}

	public void cualesfinales(Linea og_finalstates){
		for (Big_State okok : bstates) {
			String tempstate=okok.getID();
			for (String bolt : og_finalstates.dameelarraywe()) {
				if ((okok.dameelarraywe().contains(bolt))&&(!(finalstates.contains(tempstate)))) {
					finalstates.add(tempstate);
				}
			}
		}
	}
}