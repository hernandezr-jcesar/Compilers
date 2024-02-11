import java.util.*;
public class AP{
	private String cadena;
	private boolean valida=false;

	//constructores
	public AP(String cadena){
		this.cadena=cadena;
	}

	//métodos
	public void validar(){
		ArrayDeque<String> stack = new ArrayDeque<String>();
		stack.push("$");
		stack.push("E");
		this.qloop(stack,0);
		if (valida) {
			System.out.println("Valida");
		}
		else{
			System.out.println("No");
		}
	}

	public void qloop(ArrayDeque<String> old_stack, int old_ind){
//		System.out.println(old_stack);
		ArrayDeque<String> new_stack = new ArrayDeque<String>(old_stack);
		int ind=old_ind;
		char[] chtkn=this.cadena.toCharArray();	//convertir la cadena a un array de chars

		if (new_stack.peek().equals("E")) {
			new_stack.pop();
			new_stack.push("R");
			new_stack.push("M");
			this.qloop(new_stack,ind);
		}
		else if (new_stack.peek().equals("R")) {
			new_stack.push("M");
			new_stack.push("+");
			this.qloop(new_stack,ind);
			new_stack.clear();
			new_stack=old_stack.clone();
			new_stack.push("M");
			new_stack.push("-");
			this.qloop(new_stack,ind);
			new_stack.clear();
			new_stack=old_stack.clone();
			new_stack.pop();
			this.qloop(new_stack,ind);
		}
		else if (new_stack.peek().equals("M")) {
			new_stack.pop();
			new_stack.push("U");
			new_stack.push("P");
			this.qloop(new_stack,ind);
		}
		else if (new_stack.peek().equals("U")) {
			new_stack.push("P");
			new_stack.push("*");
			this.qloop(new_stack,ind);
			new_stack.clear();
			new_stack=old_stack.clone();
			new_stack.pop();
			this.qloop(new_stack,ind);
		}
		else if (new_stack.peek().equals("P")) {
			new_stack.pop();
			new_stack.push(")");
			new_stack.push("E");
			new_stack.push("(");
			this.qloop(new_stack,ind);
			new_stack.clear();
			new_stack=old_stack.clone();
			new_stack.pop();
			new_stack.push("ID");
			this.qloop(new_stack,ind);
		}
		else if (new_stack.peek().equals("ID")) {
			new_stack.pop();
			new_stack.push("V");
			new_stack.push("a");
			this.qloop(new_stack,ind);
			new_stack.clear();
			new_stack=old_stack.clone();
			new_stack.pop();
			new_stack.push("V");
			new_stack.push("b");
			this.qloop(new_stack,ind);
		}
		else if (new_stack.peek().equals("V")) {
			new_stack.push("a");
			this.qloop(new_stack,ind);
			new_stack.pop();
			new_stack.push("0");
			this.qloop(new_stack,ind);
			new_stack.pop();
			new_stack.push("b");
			this.qloop(new_stack,ind);
			new_stack.pop();
			new_stack.push("1");
			this.qloop(new_stack,ind);
			new_stack.pop();
			new_stack.pop();
			this.qloop(new_stack,ind);
		}
		else if (ind<chtkn.length) {
			String tempchartkn=Character.toString(chtkn[ind]);	//Guardar en un string el caracter en el que vamos de la cadena
			if (((tempchartkn.equals("a"))&&(new_stack.peek().equals("a")))||((tempchartkn.equals("-"))&&(new_stack.peek().equals("-")))||((tempchartkn.equals("b"))&&(new_stack.peek().equals("b")))||((tempchartkn.equals("0"))&&(new_stack.peek().equals("0")))||((tempchartkn.equals("1"))&&(new_stack.peek().equals("1")))||((tempchartkn.equals("+"))&&(new_stack.peek().equals("+")))||((tempchartkn.equals("*"))&&(new_stack.peek().equals("*")))||((tempchartkn.equals("("))&&(new_stack.peek().equals("(")))||((tempchartkn.equals(")"))&&(new_stack.peek().equals(")")))) {
				new_stack.pop();
				this.qloop(new_stack,ind+1);
			}
		}
		else if (new_stack.peek().equals("$")) {
			valida=true;
		}
	}
}