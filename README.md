# new-tasklist

## Instalação do projeto
Para realizar a instalação do projeto, dentro de seu ambiente virtual, rodar `pip install -r requirements.txt` e aguardar a instalação de todas as dependencias do projeto.
Após isso, deverá rodar o comando `python manage.py makemigrations & python manage.py migrate` para iniciar a base de dados com as tabelas do projeto. A base de dado é um sqlite simples.
Em seguida, você deverá criar um superuser rodando, dentro da pasta do projeto e com o ambiente virtual ativo, o comando `python manage.py createsuperuser`, e informar um usuário, email e senha. Após criar seu usuário, antes de iniciar a aplicação, rodar o comando `python manage.py load_status` para criar os status que serão utilizados para as tasks.

## Endpoints

### Autenticação e criação de usuario
Para autenticar seu usuário na aplicação, deverá ser realizado um `POST` no endpoint `/api/token/` com o seguinte dict:

    {
        "username": <seu usuario criado anteriormente>,
        "password": <sua senha criada anteriormente>
    }

Foi adicionada também uma API para criar um usuário, ela fica em `/users/` e recebe, em seu dict, as informações de username e password

    {
        "username": <seu usuario>,
        "password": <sua senha>
    }
Para realizar todas as funções da aplicação você deverá estar autenticado e passar o Bearer token no header da requisição.

### Status
Para criação, edição, visualização e exclusão de Status, utilizase os endpoints de `/status/` e `/status/<pk-status>`
Sendo que para criar um novo status, você deverá mandar o dict contendo:

    {
        "description": "<status>"
    }

### Task
As funções para uma task estão em `/tasks/` e `/tasks/<pk-task>`. Para criar uma task você passará um dicionário como o seguinte em uma requisição POST:

    {
        "title": "<title>",
        "description": "<description>"
    }
Ele automaticamente vai para o status_id = 1 (pelo comando load_status será o "To Do"), e é salvo para o usuário que está criando a task.

Para alterar uma task, é necessária uma requisição do tipo PATCH passando somente os dados que serão alterados.
Como por exemplo:

    {
        "status": <id-status>
    }

Exclusão é esperada uma request do tipo DELETE, e listagem e detail são no GET.

## Deploy
Foi feito o deploy da aplicação no Heroku (https://new-tasklist-evoe.herokuapp.com/) e foram criados os seguintes usuários para teste:

username: userteste
password: password123

username: userteste2
password: password123