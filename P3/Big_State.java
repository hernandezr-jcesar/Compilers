import java.util.*;
public class Big_State{		//un Big_State es 
	private String id;
	private ArrayList<String> states;

	//constructor
	public Big_State(String id, ArrayList<String> states){
		this.id=id;
		this.states = new ArrayList<String>(states);
	}

	//métodos
	//existe?

	public String toString(){					//regresa los elementos del arraylist en String
		return (""+id+"\t"+states);
	}

	public ArrayList<String> dameelarraywe(){	//regresa todo el arraylist "states"
		return states;
	}

	public String singleelement(int ind){	//regresa un solo elemento del arraylist elementos, siendo ind el índice
		return (states.get(ind));
	}

	public String getID(){
		return id;
	}
}