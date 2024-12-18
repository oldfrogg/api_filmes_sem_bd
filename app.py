# Projeto desenvolvido para auxílio no estudo de Python, utilizando como base o curso da Alura: Flask: crie uma webapp com Python, com o instrutor Bruno Divino

# Esta API no estado atual, retorna dados em formato HTML. Futuramente, ao desenvolver melhor a aplicação, colocarei retorno em JSON, para possibilitar seu consumo por outras aplicações front-end.


from flask import Flask, render_template, request, redirect, session, flash, url_for
# render_template para renderizar o arquivo HTML. Já irá esperar um diretório chamado "templates" com os HTMLs dentro
# request para pegar os dados do form dos arquivos HTML, que terão o method=post e action apontando para a rota que descreverei aqui. A referência é o que está no name dos inputs
# redirect para redirecionar as rotas intermediárias para rotas que tenham renderização de templates.
# session para reter informações por mais de um ciclo de request. Precisarei para verificar sempre se o usuário está logado. Guardará isso nos cookies do navegador.
# flash para exibir mensagens rápidas na tela para o usuário
# url_for para auxiliar na manutenção do código, evitando ter que alterar o nome de uma rota em mais de um local, caso eu precise alterar o nome da rota, pois nos redirects marcarei \
    # ... o nome da função, ao invés da rota no decorador. Boa prática.

app = Flask(__name__) #instancio o Flask

# Sempre que o cliente retorna os cookies ao servidor, Flask verifica se a assinatura ainda é válida. Se os dados ou a assinatura forem modificados, o Flask rejeita o cookie, protegendo contra manipulações.
app.secret_key = "gipao" 

# Criando a classe "Filme"
class Filme:
    def __init__(self, nome, genero, ano):
        self.nome = nome 
        self.genero = genero 
        self.ano = ano


# Criando as instâncias da classe Filme
filme1 = Filme('O Poderoso Chefão', 'Drama', '1972')
filme2 = Filme('Harry Potter', 'Ficção Científica', '2000')
filme3 = Filme('O Grande Gatsby', 'Romance', '2013')
filme4 = Filme('Transformers', 'Ficção Científica', '2009')
filme5 = Filme('Interestelar', 'Ficção Científica', '2013')

# Colocando em lista, para facilitar a apresentação, diminuindo código
lista_de_filmes = [filme1, filme2, filme3, filme4, filme5]

titulo="Filmes"  # Titulo no <h1> da pagina

# Criando a classe "Usuario", para definir os usuários que podem mexer no site
class Usuario:
    def __init__(self, nick, senha):
        self.nick = nick
        self.senha = senha
        
# Instanciando os usuários que podem utilizar o site        
usuario1 = Usuario("Vascaino", "Vasco")
usuario2 = Usuario("Colorado", "Sergipe")

# Faço um dicionário ligando a chave (nick do usuário) ao valor (usuário, todos os dados), para facilitar o uso.  O nick vai ser a chave para levar ao usuário
usuarios = { usuario1.nick : usuario1,
            usuario2.nick : usuario2,
            }


# Rota raiz, mostrará a lista de filmes
@app.route('/')
def index():
    return render_template('home.html', titulo=titulo, filmes=lista_de_filmes)


# Rota que mostrará o HTML que terá os inputs para adicionar novos filmes
@app.route('/novo_filme')
def novo_filme():
    if 'usuario_logado' not in session or session['usuario_logado'] == None: # Verifico se há um usuário logado ativo. Caso não, mando para o login. Caso sim, vai para a pag desejada.
        return redirect(url_for('login', proxima=url_for('novo_filme')))  # Redireciono para o login, mandando como query a indicação do caminho da pagina que o usuário pretendia
    return render_template('novo_filme.html', titulo=titulo)


# Rota intermediária que executará a função de adicionar um filme à lista
@app.route('/criar', methods=["POST", ]) # É preciso indicar que irá utilizar o POST, pois o padrão é GET, e sem isso teríamos como retorno "METHOD NOT ALLOWED"
def criar():
    nome_filme = request.form["filme"]
    genero_filme = request.form["genero"]
    ano_filme = request.form["ano"]
    # Capturei os inputs 
    filme = Filme(nome_filme, genero_filme, ano_filme)
    # Instanciei a classe
    lista_de_filmes.append(filme)
    # Adicionei à lista
    return redirect(url_for('index'))
    # Redireciono para a home, pois se não eu continuaria na rota intermediária, e o formulário sempre tentaria ser enviado novamente
    


# Login
@app.route('/login', methods=["GET", ])
def login():
    proxima = request.args.get('proxima') or url_for('index') # Deixo esse or, para evitar que dê erro, caso o usuário acesse direto a rota de login, sem passar por outra rota.
    return render_template('login.html', proxima=proxima)


# Rota intermediária de autenticação
@app.route('/autenticar', methods=["POST", ])
def autenticar():
    usuario = request.form['nomeusuario']
    proxima_pag = request.form['proxima']
    if usuario in usuarios:
        if request.form['senhausuario'] == usuarios[usuario].senha:
            session['usuario_logado'] = usuarios[usuario].nick
            flash(session['usuario_logado'] + ' logado com sucesso')
            return redirect(proxima_pag)
        else:
            flash("Senha incorreta!")
            return redirect(url_for('login', proxima=proxima_pag))
    else:
        flash("Usuário não cadastrado!")
        return redirect(url_for('login', proxima=proxima_pag))


# Logout
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


# Executará a aplicação, caso ela não tenha sido importada em outro projeto
if __name__ == "__main__":
    app.run(debug=True)