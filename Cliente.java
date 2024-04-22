import java.util.Collection;
import java.util.Vector;
import java.util.Iterator;


public class Cliente {
  private String nome;
  public Collection<Aluguel> fitasAlugadas = new Vector<Aluguel>();
  
  public Cliente(String nome) {
    this.nome = nome;
  }

  public String getNome() {
    return nome;
  }
  public void adicionaAluguel(Aluguel aluguel) {
    fitasAlugadas.add(aluguel);
  }
  public String obterTituloFilmesAlugados(){
    Iterator<Aluguel> alugueis = fitasAlugadas.iterator();
    String titulos = "";
    while (alugueis.hasNext()) {
      Aluguel cada = alugueis.next();
       String titulo = cada.getTitulo();
       titulos = titulo + ",";
      
    }
    return titulos;

  }

  public String extrato() {
    final String fimDeLinha = System.getProperty("line.separator");
    double valorTotal = 0.0;
    int pontosDeAlugadorFrequente = 0;
    
    String resultado = "Registro de Alugueis de " + getNome() + fimDeLinha;
    
    Iterator<Aluguel> alugueis = fitasAlugadas.iterator();
    while(alugueis.hasNext()) {
      Aluguel cada = alugueis.next();
      double valorCorrente = 0.0;
      Fita chamada = new Fita(cada.fita.titulo, cada.fita.codigoDePreco) ;
      chamada.getValorCorrente(cada, valorCorrente);

      pontosDeAlugadorFrequente++;
      if(cada.getFita().getCodigoDePreco() == Fita.LANCAMENTO &&  
         cada.getDiasAlugada() > 1) {
           pontosDeAlugadorFrequente++;
      }

      resultado += cada.getFita().getTitulo() + ":" + valorCorrente + fimDeLinha;
      valorTotal += valorCorrente;
    } // fim do while
    
    resultado += "Valor total devido: " + valorTotal + fimDeLinha;
    resultado += "Voce acumulou " + pontosDeAlugadorFrequente + " pontos" + fimDeLinha;
    return resultado;
  }

}

