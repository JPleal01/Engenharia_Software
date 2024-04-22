

class Usuario:
    
    blogs = []
    def __init__(self, email) -> None:
        self.__email=email
    def inserir_novo_blog(self, blog: 'Blog'):
        self.blogs.append[blog]




class Blog:
    notas = []
    def __init__(self, titulo, data_criacao, dono:'Usuario', idblog) -> None:
        self.__titulo = titulo
        self.__data_criacao = data_criacao
        self.__dono = dono(Usuario)
        self.__idblog = idblog
    
    def get_idblog(self,texto, data_criacao_nota):
        return self.__idblog
    def criar_nota(self,texto, data_criacao_nota):
        nota= Nota(texto, data_criacao_nota)
    def inserir_nova_nota(self, nota: 'Nota'):
        self.notas.append[nota]
    def get_textos_notas(self):
        for nota in self.notas:
            texto_nota = Nota.get_texto()
            return texto_nota

    def buscar_nota_por_id(self, idnota):
        for nota in self.notas:
            if nota.get_idnota == idnota:
                return nota
    def criar_novo_comentario(self, texto, data_criacao, autor,idnota):
        nota = self.buscar_nota_por_id(idnota)



class Comentario:
    def __init__(self, texto, data_criacao, autor) -> None:
        self.__texto = texto
        self.__data_criacao = data_criacao
        self.__autor = autor

class Nota:

     
    comentarios_da_nota = []

    def __init__ (self, texto, data_criacao, idnota):
        self.__texto= texto
        self.__data_criacao = data_criacao
        self.__idnota = idnota

    def get_texto(self):
        return self.__texto
    def get_idnota(self):
        return self.__idnota
    def criar_novocomentario(self, texto, data_criacao, autor:'Usuario'):
        comentario = Comentario(self.texto, self.data_criacao, self.autor)
        self.inserir_novo_comentario(comentario)

    def inserir_novo_comentario(self, comentario:Comentario):
        self.comentarios_da_nota.append[comentario]

class Sistema:
    import Blog
    usuarios =[]
    blogs = []
    def __init__(self) -> None:
        pass
        # self.__usuarios = []
        # self.__blogs = []
    def inserir_novo_usuario(self, usuario:Usuario):
        self.usuarios.append[usuario]
    
    def inserir_novo_blog(self, blog:Blog):
        self.blogs.append[blog]

    def criar_blog(self, titulo, data_criacao, dono, idblog):
        blog = Blog(self.titulo, self.data_criacao, self.dono, self.idblog)
        self.inserir_novo_blog(blog= blog)

    def buscar_blog_por_id(self, idblog):
        for blog in self.blogs:
            if blog.get_idblog == idblog:
                return blog
        return None
    def criar_nota(self,texto,data_criacao,idblog):
        self.buscar_blog_por_id(idblog)
        Blog.criar_nota(texto, data_criacao)
  
    def buscar_texto_nota(self,idblog):
        blog =self.buscar_blog_por_id(idblog)
        blog.get_textos_notas()

    def criar_comentario(self,texto,data_criacao,idblog, idnota, autor):
        blog = self.buscar_blog_por_id(idblog)
        blog.criar_novo_comentario()

    