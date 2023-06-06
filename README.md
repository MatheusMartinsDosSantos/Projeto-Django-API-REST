# Projeto Django API REST
# Grupo: Matheus Martins dos Santos, Lucas Correia da Cruz, Lucas Martins, Gusttavo Orsi

===========Tema===========
Um sistema que adiciona, atualiza, deleta e lista livros de uma blibioteca.
========Instruções========
Para usar esse sistema, é necessario o uso do aplicativo Insomnia, para poder realizar todas suas funções.

1. Iniciar o Servidor.

Abrir o cmd
Entrar no diretorio onde está o projeto, através do comando "cd <Insira o diretorio aqui>". 
Executar as migrações do servidor com o comando "python manage.py migrate"
Iniciar o servidor através do comando "python manage.py runserver"
Com isso o servidor estará rodando.

2. Abrir as configurações do Insomnia.

Abrir o Insomnia.
Apertar "New Document" na parte superior do aplicativo e depois clicar na opção "Import/Export"
Importar o arquivo "Config Insomnia"

3. Realizar as funções do sistema

  1. Adicionar Livros
     
     Abra o request "Adicionar Livro"
     Ira aparecer:
     "{
     "title": "Inserir Titulo",
     "author": "Inserir Autor",
     "publication_date": "Inserir Data"
     }"
     Aqui é possível inserir o titulo, o nome do autor, e a data de publicação do livro.
     Apóss inserir o que deseja, aperte "Send"
     Após isso, o livro ira ser adicionado.

  2. Remover Livros
      
     Abra o request "Deletar Livro"
     No link que está no request, ira aparecer: "http://localhost:8000/api/books/<id>/delete/"
     Altere no link a parte "<id>" para o id do livro que deseja deletar.
     Aperte Send apos inserir o id desejado.
     Após isso, o livro ira ser deletado.

  3. Atualizar Livros
      
     Abra o request "Atualizar Livro"
     Ira aparecer:
     {
     "title": "Inserir Titulo",
     "author": "Inserir Autor"
     }
     Aqui é possível inserir o novo titulo e o novo nome do autor.
     Depois, altere no link, a parte "<id>" para o id do livro que deseja atualizar.
     Aperte Send apos inserir o id desejado.
     Após isso, o livro ira ser atualizado.

  4. Listar Livros

     Abra o request "Listar Livro"
     Aperte Send
     Após isso, todos os livros irão ser listados.

  5. Listar um Livro em especifico.

     Abra o request "Listar Livro Especifico"
     No link que está no request, ira aparecer: "http://localhost:8000/api/books/<id>/"
     Altere no link a parte "<id>" para o id do livro que deseja listar.
     Aperte Send
     Após isso, o livro que escolheu ira ser listado.

 