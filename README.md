# Projeto Comercio Eletrônico
 
 ![](https://i.imgur.com/RYAUU8q.png)

 
## Links 
* [Django](https://www.djangoproject.com/) - Django Web Framework versão 4.0.6
* [Python](https://www.python.org/) - Python versão 3.8.10
* [SQLite](https://www.sqlite.org/index.html) - banco de dados SQL embutido 3.3.3
* [Git](https://git-scm.com/) - sistema de controle de versão 2.25.1
* [Pillow](https://pypi.org/project/Pillow/)- Python Imaging Library adiciona recursos de processamento de imagem ao seu interpretador Python


## Pacotes
- [x] Django
- [x] SQLite(Database)
- [x] Html
- [x] CSS
- [x] Javascript
- [x] Pillow


## Pacotes

Arquivos padrões
`manage.py`

É um utilitário de linha de comando que permite interagir com o projeto e app django de várias maneiras.
Projeto

O projeto é uma coleção de configurações e apps para um site, que nesse caso é o:
`blog`

Dentro da pasta do projeto do django temos os seguintes arquivos:
`__init__.py`

Arquivo vazio que indica ao python que este diretório deve ser considerado como um pacote.
`settings.py`

Arquivo de configuração do projeto django, aqui você adiciona os apps, banco de dados, etc.
`urls.py`

Arquivo onde declara as urls e rotas dos apps que estão relacionados ao respectivo projeto django. Por padrão tem a rota para o admin.py declarada
`asgi.py`

Ponto de integração entre servidores web compatíveis com ASGI e a aplicação python.
`wsgi.py`

# Aplicação

O app é uma aplicação que realiza uma determinada função, que nesse caso são: 

`posts`, `comentarios`, `categoria`

Observação: Um projeto pode conter muitos apps e um app pode estar em múltiplos projetos

Dentro da pasta de app do django temos os seguintes arquivos:
`__init__.py` 

Arquivo vazio que indica ao python que este diretório deve ser considerado um pacote python.
`admin.py`

É o arquivo para registrar a área administrativa do site, nele tem um crud do modelo do banco de dados da aplicação que está em model.py. Para ser acessado tem que criar uma conta admin com o comando python3 manage.py createsuperuser
`apps.py`

Arquivo responsável pela configuração do app do projeto django.
`migrations/` 

As migrations estão relacionadas aos banco de dados, é a maneira do django de propagar as alterações feitas em seus modelos no models.py (adicionando um campo, excluindo um modelo, etc.) em seu esquema de banco de dados.
`models.py` 

 
## Configuraçes para rodar a aplicação

instalar o python
instalar o pip(gerenciador de pacotes)

python3 -m venv nome_do_ambiente_virtual

source nome_do_ambiente_virtual/bin/activate(linux)
nome_do_ambiente_virtual\Scripts\Activate(windows)

# Após os passos acima: 
Entrar no diretório do ambiente_virtual
e fazer python manage.runserver ou ./manage.py runserver 


