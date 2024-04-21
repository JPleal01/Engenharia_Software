

public class Fita {
  public static final int NORMAL = 0;
  public static final int LANCAMENTO = 1;
  public static final int INFANTIL = 2;

  public String titulo;
  public int codigoDePreco;

  public Fita(String titulo, int codigoDePreco) {
    this.titulo = titulo;
    this.codigoDePreco = codigoDePreco;
  }



public String getTitulo() {
    return titulo;
  }

  public int getCodigoDePreco() {
    return codigoDePreco;
  }

  public void setCodigoDePreco(int codigoDePreco) {
    this.codigoDePreco = codigoDePreco;
  }
  public double getValorCorrente(Aluguel cada, double valorCorrente){
    
    switch(cada.getFita().getCodigoDePreco()) {
      case Fita.NORMAL:
        valorCorrente += 2;
        if(cada.getDiasAlugada() > 2) {
          valorCorrente += (cada.getDiasAlugada() - 2) * 1.5;
        }
        break;
      case Fita.LANCAMENTO:
        valorCorrente += cada.getDiasAlugada() * 3;
      break;
      case Fita.INFANTIL:
        valorCorrente += 1.5;
        if(cada.getDiasAlugada() > 3) {
          valorCorrente += (cada.getDiasAlugada() - 3) * 1.5;
        }
      } // fim do switch
    return valorCorrente;

  }

  }

