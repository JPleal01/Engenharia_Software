class Usuario:
    email = ""
    comentarios = []

class Blog:
    titulo =""
    data_criacao = ""
    dono = Usuario() 

class Nota:
    texto = ""
    data_criacao = ""
    comentarios_da_nota = []

class Comentario:
    texto = ""
    data_criacao = ""


class Sistema:
    usuarios = []
    blogs = []