class Usuario:
    email = ""
    blogs = []

class Blog:
    titulo =""
    data_criacao = ""
    dono = Usuario() 

class Comentario:
    texto = ""
    data_criacao = ""

class Nota:
    texto = ""
    data_criacao = ""
    comentarios_da_nota = [Comentario]


class Sistema:
    usuarios =[Usuario]
    blogs = [Blog]