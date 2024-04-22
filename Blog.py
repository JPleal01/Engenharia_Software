

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

class Comentario:
    def __init__(self, texto, data_criacao) -> None:
        self.__texto = texto
        self.__data_criacao = data_criacao

class Nota:

    def __init__ (self, texto, data_criacao):
        self.__texto= texto
        self.__data_criacao = data_criacao
    def get_texto(self):
        return self.__texto
    
    
    comentarios_da_nota = []

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

    def criar_blog(self, titulo, data_criacao, dono):
        blog = Blog(self.titulo, self.data_criacao, self.dono)
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
        self.buscar_blog_por_id(idblog)
        Blog.get_textos_notas()
    