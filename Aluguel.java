
public class Aluguel {
  public Fita fita;
  public int diasAlugada;

  public Aluguel(Fita fita, int diasAlugada) {
    this.fita = fita;
    this.diasAlugada = diasAlugada;
  }

  public Fita getFita() {
    return fita;
  }

  public int getDiasAlugada() {
    return diasAlugada;
  }

  public String getTitulo(){
    fita = new Fita(getTitulo(), diasAlugada);
    String titulo = fita.getTitulo();
    return titulo;
  }

}

