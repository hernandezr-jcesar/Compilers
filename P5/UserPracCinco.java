import java.util.*;
public class UserPracCinco{
	public static void main(String[] args) {

		System.out.println("Ingresar cadena a validar:");
		Scanner entrada = new Scanner(System.in); 
		String input=entrada.nextLine();
		AP ap = new AP(input);
		ap.validar();
	}
}