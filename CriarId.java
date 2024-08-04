public class CriarId {
    public static void criarid(Pessoa usuario){
    	System.out.println("Seu id de usuario é " + usuario.getPrimeiroNome().substring(0, 1) + usuario.getUltimoNome());
    }
    
}
