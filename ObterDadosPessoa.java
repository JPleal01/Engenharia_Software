import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ObterDadosPessoa {
    
    public static Pessoa obterdados() throws IOException{
        
        Pessoa pessoa = new Pessoa();
		BufferedReader teclado = new BufferedReader(new InputStreamReader(System.in));
		
		System.out.println("Qual é seu primeiro nome?");
		pessoa.setPrimeiroNome(teclado.readLine());
		
		System.out.println("Qual é seu ultimo nome?");
		pessoa.setUltimoNome(teclado.readLine());

        return pessoa;


    }

}
