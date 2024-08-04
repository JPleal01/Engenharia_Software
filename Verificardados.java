public class Verificardados {
    
    public static boolean validapessoa(Pessoa pessoa){

        if (pessoa.getPrimeiroNome().isEmpty()) {
			System.out.println("Você nao forneceu um primeiro nome valido");
	
			return  false;
		}
		
		if (pessoa.getUltimoNome().isEmpty()) {
			System.out.println("Voce nao forneceu um ultimo nome valido");
			return false;
		}
        return true;
    }
}
