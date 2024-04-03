class Comentario:
    texto = ""
    data_criacao = ""

class Usuario:
    email = ""
    comentarios = [Comentario]

class Blog:
    titulo =""
    data_criacao = ""
    dono = Usuario() 

class Nota:
    texto = ""
    data_criacao = ""
    comentarios_da_nota = [Comentario]


class Sistema:
    usuarios =[Usuario]
    blogs = [Blog]