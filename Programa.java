import java.io.IOException;


public class Programa {

	public static void main(String[] args) throws IOException {
		
		GerenciadorMensagem.mensagemdebemvido();
		
		Pessoa usuario = ObterDadosPessoa.obterdados();

		
		
		if (Verificardados.validapessoa(usuario) == false ){
			GerenciadorMensagem.mensagemfimdeprograma();
			return;
		}
		
		// Cria um id para o usu�rio
		CriarId.criarid(usuario);
		GerenciadorMensagem.mensagemfimdeprograma();
		
	}

}