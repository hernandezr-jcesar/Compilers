import java.util.*;
class Test
{

	public static void main(String[] args)
	{
		ArrayList<String> okok = new ArrayList<String>();
		for (int i=13;i>=0 ; i--) {
			String temp=(""+i);
			okok.add(temp);
		}
		System.out.println(okok);
		Collections.sort(okok);
		System.out.println(okok);
	}
}