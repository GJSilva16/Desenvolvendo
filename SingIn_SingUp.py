# Biblioteca de interface do Python
from tkinter import *
# Biblioteca de banco de dados do Python
import sqlite3

# Classe que contem as funões do código.
class tela:
    # Função que inicia a interação chamando a tela para login.
    def __init__(self):

        self.telaInicial = Tk()
        self.telaInicial.title('Oliveira Trade')
        self.telaInicial.geometry('300x150')

        self.label1 = Label(self.telaInicial, text='Usuario')
        self.label1.place(x=40, y=10)
        self.usuario = Entry(self.telaInicial, bd=5)
        self.usuario.place(x=100, y=10)

        self.label2 = Label(self.telaInicial, text='Senha')
        self.label2.place(x=40, y=40)
        self.senha = Entry(self.telaInicial, bd=5, show='*')
        self.senha.place(x=100, y=40)

        self.botaoEntrar = Button(self.telaInicial, text='Entrar', bd=3, command=self.Verificar)
        self.botaoEntrar.place(x=100, y=100)

        self.botaoCadastrar = Button(self.telaInicial, text='Cadastrar', bd=3, command=self.CadastrarUsuario)
        self.botaoCadastrar.place(x=170, y=100)
        self.telaInicial.mainloop()

    # Função de acesso aos dados no banco, verificação de usuario e senha, chama a função "Logado" que abre uma tela
    # com a mensagem "Usuario logado com sucesso!" e fecha a tela de login se o usuario e senha estiverem corretos,
    # se não estiverem chama a fução "Erro" que abre uma tela com a mensagem "dados estão incorretos!".
    # Chamada no botão "Entrar" na tela de login na função "__init__".
    def Verificar(self):

        try:
            connection = sqlite3.connect('dados.db')
            cursor = connection.cursor()

            cursor.execute("SELECT senha FROM usuarios WHERE usuario = '{}'".format(self.usuario.get()))
            senhabd = cursor.fetchall()

            connection.close()

            if self.senha.get() == senhabd[0][0]:
                self.Logado()
                self.telaInicial.destroy()
            else:
                self.Erro()
                self.telaInicial.destroy()
        except:
            self.NovoUsuario()

    # Função fecha a tela de login e chama a função "Cadastrar" que abre uma tela para o cadastro dos dados do usuario.
    # Chamada no botão "Cadastrar" na tela de login na função "__init__".
    def CadastrarUsuario(self):

        self.telaInicial.destroy()
        self.Cadastrar()

    # Função que chama a tela com a mensagem "Usuario logado com sucesso!".
    # Chamada na função "Verificar" se o usuario e senha estiverem corretos.
    def Logado(self):

        self.telaLogado = Tk()
        self.telaLogado.title('Obrigado!')
        self.telaLogado.geometry('300x100')

        self.menssagem = Label(self.telaLogado, text='Usuario Logado com sucesso!')
        self.menssagem.place(x=60, y=20)

        self.botaoEncerrar = Button(self.telaLogado, text='OK', bd=3, command=self.Terminar)
        self.botaoEncerrar.place(x=120, y=60)

    # Função que abre uma tela com a mensagem "Os dados inseridos estão incorretos!".
    # Chamada na função "Verificar" se o usuario e senha não estiverem corretos.
    def Erro(self):

        self.telaErro = Tk()
        self.telaErro.title('Dados incorretos!')
        self.telaErro.geometry('300x100')

        self.menssagem1 = Label(self.telaErro, text='Os dados inseridos estão incorretos!')
        self.menssagem1.place(x=50, y=10)

        self.botaoEncerrar1 = Button(self.telaErro, text='OK', bd=3, command=self.Retornar)
        self.botaoEncerrar1.place(x=120, y=50)

    # Função abre uma tela com a mensagem "Usuario não cadastrado!".
    # Chamada na função "NovoUsuario", se o usuario não estiver cadastrado.
    def SemCadastro(self):

        self.telaErroCadastro = Tk()
        self.telaErroCadastro.title('Usuario não cadastrado!')
        self.telaErroCadastro.geometry('400x100')

        self.menssagem2 = Label(self.telaErroCadastro, text='Usuario não cadastrado. Por favor, efetue o cadastro!')
        self.menssagem2.place(x=60, y=10)

        self.botaoCadastrar1 = Button(self.telaErroCadastro, text='Cadastrar', bd=3, command=self.Cadastro)
        self.botaoCadastrar1.place(x=150, y=50)

    # Função que fecha a tela com a mensagem "Login efetuado com sucesso!".
    # Chamada no botão "OK" da mesma tela na função "Logado".
    # Finaliza o processo.
    def Terminar(self):

        self.telaLogado.destroy()

    # Função que fecha a tela com a mensagem "Os dados inseridos estão incorretos!" e chama a função "__init__" que
    # abre a tela para login.
    # Chamada no botão "OK" da tela com a mensagem "Os dados inseridos estão incorretos!" na função "Erro".
    def Retornar(self):

        self.telaErro.destroy()
        self.__init__()

    # Função que fecha a tela de login e chama a função "SemCadastro" que abre uma tela com a mensagem "Usuario não
    # cadastrado. Por favor, efetue o cadastro!"
    # Chamada na função "Verificar", se os dados não forem encontrados no banco.
    def NovoUsuario(self):

        self.telaInicial.destroy()
        self.SemCadastro()

    # Função que fecha a tela com a mensagem "Usuario não cadastrado. Por favor, efetue o cadastro!" e chama a função
    # "Cadastrar" que abre uma tela para o cadastro dos dados do usuario.
    # Chamada no botão "Cadastrar" da tela com a mensagem "Usuario não cadastrado. Por favor, efetue o cadastro!" na
    # função "SemCadastro"
    def Cadastro(self):

        self.telaErroCadastro.destroy()
        self.Cadastrar()

    # Função que cria a tela para cadastro do usuario.
    # Chamada nas funções "CadastrarUsuario" e "Cadastro".
    def Cadastrar(self):

        self.telaCadastro = Tk()
        self.telaCadastro.title('Preencha seus dados')
        self.telaCadastro.geometry('500x330')

        self.dados1 = Label(self.telaCadastro, text='Nome')
        self.dados1.place(x=40, y=10)
        self.nome = Entry(self.telaCadastro)
        self.nome.place(x=180, y=10, width=300)

        self.dados2 = Label(self.telaCadastro, text='Idade')
        self.dados2.place(x=40, y=40)
        self.idade = Entry(self.telaCadastro)
        self.idade.place(x=180, y=40, width=300)

        self.dados3 = Label(self.telaCadastro, text='CPF')
        self.dados3.place(x=40, y=70)
        self.cpf = Entry(self.telaCadastro)
        self.cpf.place(x=180, y=70, width=300)

        self.dados4 = Label(self.telaCadastro, text='Email')
        self.dados4.place(x=40, y=100)
        self.email = Entry(self.telaCadastro)
        self.email.place(x=180, y=100, width=300)

        self.dados5 = Label(self.telaCadastro, text='Fone')
        self.dados5.place(x=40, y=130)
        self.fone = Entry(self.telaCadastro)
        self.fone.place(x=180, y=130, width=300)

        self.dados6 = Label(self.telaCadastro, text='Cidade')
        self.dados6.place(x=40, y=160)
        self.cidade = Entry(self.telaCadastro)
        self.cidade.place(x=180, y=160, width=300)

        self.dados7 = Label(self.telaCadastro, text='UF')
        self.dados7.place(x=40, y=190)
        self.uf = Entry(self.telaCadastro)
        self.uf.place(x=180, y=190, width=300)

        self.dados8 = Label(self.telaCadastro, text='Usuario')
        self.dados8.place(x=40, y=220)
        self.usuario1 = Entry(self.telaCadastro)
        self.usuario1.place(x=180, y=220, width=300)

        self.dados9 = Label(self.telaCadastro, text='Senha')
        self.dados9.place(x=40, y=250)
        self.senha1 = Entry(self.telaCadastro)
        self.senha1.place(x=180, y=250, width=300)

        self.botaoSalvar = Button(self.telaCadastro, text='Salvar', bd=3, command=self.VerificarCampo)
        self.botaoSalvar.place(x=180, y=280)

    # Função que cria o banco de dados caso não exista e conecta esse banco de dados. Cria a tabela caso não exista e insere os valores
    # digitados na tela de cadastro função "Cadastrar".
    # Chamada na função "VerificarCampo" se o usuario não deixar nenhum campo em branco.
    def Salvar(self):

        connection = sqlite3.connect('dados.db')
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome VARCHAR(100), idade VARCHAR(3), '
                       'cpf CHAR(11), email VARCHAR(60),  fone VARCHAR(11), cidade VARCHAR(20), uf CHAR(2), usuario VARCHAR(100), senha VARCHAR(20))')

        self.infos = (self.nome.get(), self.idade.get(), self.cpf.get(), self.email.get(), self.fone.get(), self.cidade.get(), self.uf.get(),
                      self.usuario1.get(), self.senha1.get())

        cursor.execute("INSERT INTO usuarios VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)", self.infos)

        connection.commit()
        connection.close()

        self.telaCadastro.destroy()
        self.CadastroSucesso()

    # Função verifica se o campo esta vazio, se estiver chama a função "ErroVazio" que abre uma tela com a mensagem
    # "Por favor, preencha todos os campos!", se não chama a função "Salvar" que cria caso não exista e conecta o banco
    # de dados. Cria a tabela caso não exista e insere os valores digitados na tela de cadastro função "Cadastrar".
    # Chamada no botaõ "OK" da tela de cadastro função "Cadastrar".
    def VerificarCampo(self):

        if self.nome.get() == '' or self.idade.get() == '' or self.cpf.get() == '' or self.email.get() == '' or self.fone.get() == ''\
                or self.cidade.get() == '' or self.uf.get() == '' or self.usuario1.get() == '' or self.senha1.get() == '':
            self.ErroVazio()
        else:
            self.Salvar()

    # Função que abre uma tela com a mensagem "Cadastro efetuado com sucesso!".
    # Chamada pela função "Salvar" que cria o banco de dados caso não exista e conecta com esse banco de dados. Cria a tabela caso não exista e insere os valores
    # digitados na tela de cadastro função "Cadastrar".
    def CadastroSucesso(self):

        self.telaCadastroSucesso = Tk()
        self.telaCadastroSucesso.title('Obrigado!')
        self.telaCadastroSucesso.geometry('300x100')

        self.menssagem3 = Label(self.telaCadastroSucesso, text='Cadastro efetuado com sucesso!')
        self.menssagem3.place(x=40, y=10)

        self.botaoConfirmar = Button(self.telaCadastroSucesso, text='OK', bd=3, command=self.PosCadastro)
        self.botaoConfirmar.place(x=120, y=50)

    # Função que fecha a tela com a mensagem "Cadastro efetuado com sucesso!" função "CadastroSucesso" e chama a função
    # "__init__" que abre a tela login.
    # Chamada no botão "OK" da tela com a mensagem "Cadastro efetuado com sucesso!" função "CadastroSucesso".
    def PosCadastro(self):

        self.telaCadastroSucesso.destroy()
        self.__init__()

    # Função que abre a tela com a mensagem "Por favor, preencha todos os campos!".
    # Chamada na função "VerificarCampo" se o usuario deixar algum campo em branco.
    def ErroVazio(self):

        self.telaErroVazio = Tk()
        self.telaErroVazio.title('Atenção!')
        self.telaErroVazio.geometry('300x100')

        self.menssagem4 = Label(self.telaErroVazio, text='Por favor, preencha todos os campos!')
        self.menssagem4.place(x=40, y=10)

        self.botaoCadastrar2 = Button(self.telaErroVazio, text='OK', bd=3, command=self.RetornarCadastro)
        self.botaoCadastrar2.place(x=120, y=50)

    # Função que fecha a tela com a mensagem "Por favor, preencha todos os campos!" função "ErroVazio".
    # Chamada no botão "OK" da mesma tela.
    def RetornarCadastro(self):

        self.telaErroVazio.destroy()

tela()
