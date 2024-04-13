# Engenharia_Software
### Diagrama UML e Codigo em Java de um sistema basico de blog.
***
Considere os requisitos do sistema de blog descritos abaixo. Desenhe o diagrama de classes em alguma ferramenta de sua preferência (sugestão draw.io). No diagrama, desenhar as classes, atributos, relacionamentos, multiplicidade e navegabilidade. Nas classes, basta colocar os atributos. Não é necessário colocar métodos.

Além disso, escreva o código correspondente ao diagrama de classes em qualquer linguagem orientada a objetos.

Faça aqui na atividade o upload da imagem do diagrama (arquivo de imagem) e dos arquivos do código fonte. 

**Requisitos**

Um blog tem um título e uma data de criação e além disso é um conjunto de conteúdos.

Estes conteúdos podem ser notas ou comentários sobre as notas. Tanto notas quanto comentários têm características comuns como o texto e a data de sua criação.

Todo usuário possui um e-mail que deve ser único, ou seja, não há mais de um usuário com o mesmo e-mail).

**O sistema deve:**

Permitir a criação de blogs
Permitir a utilização de blogs
Qualquer usuário pode ler conteúdos
Somente o dono do blog pode criar notas
Qualquer usuário pode criar comentários. Para criar um comentário o usuários precisa ler as notas.
Somente o dono do blog pode remover conteúdos. Para remover um conteúdo ele precisará ler o conteúdo. Caso ele remova um comentário, o autor do comentário deve ser notificado por e-mail.
***


### Correção de codigo segundo padrões GRASP- Expert. Codigo fornecido pelo professor