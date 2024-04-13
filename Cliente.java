import java.util.Collection;
import java.util.Vector;

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
}

