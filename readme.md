# API Filmes

Projeto desenvolvido para auxílio no estudo de Python, utilizando como base o curso da Alura: Flask: crie uma webapp com Python, com o instrutor Bruno Divino

Este webapp que retorna páginas HTML, onde podemos fazer o cadastro de filmes em uma lista.

Futuramente, em outro repositório, irei fazê-la retornar dados em .json, para permitir que outras aplicações front-end a consumam.
Além disso, adicionarei mais rotas, farei a verificação dos dados informados pelo usuário, utilizarei um BD, documentarei em Swagger, etc.


## Como rodar em sua máquina

Navegue até o diretório onde baixou o repositório, via algum prompt de comando
Crie um ambiente virtual
> python -m venv venv /// ou python3 -m venv venv

Ative o ambiente virtual
> .\venv\Scripts\activate (WINDOWS)  /// source venv/bin/activate (LINUX)

Instale o Flask
> pip install flask

Ou, caso prefira, pode instalar diretamente todos os requisitos. Porém, neste projeto, temos apenas o flask e seus complementos.
> pip install -r requirements.txt

Execute a aplicação
> flask run

## Rotas

* / - GET - Página inicial - Lista os filmes.
* /novo_filme - GET - Carrega a página com o template para adição de novos filmes.
* /criar - POST - Rota intermediária que executará a função de a dicionar um filme à lista.
* /login - GET - Carrega a página com o template da tela de login.
* /autenticar - POST - Rota intermediária de autenticação.
* /logout - GET - Rota que faz o logout.
