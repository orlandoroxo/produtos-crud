# Projeto Cadastro de Produtos 

O projeto Cadastro de Produtos trata-se de um sistema desenvolvido na disciplina de Desenvolvimento Rápido de Aplicações em Python para realizar as operações CRUD de produtos como requisito parcial de aprovação na disciplina. 

* Data: 02/11/2023
* Versão atual: 1.0

## 1. Pré-Requisitos

* Windows 10 ou 11.
* [Python 3.11](https://www.python.org/downloads/release/python-3110/)
* [PostgreSQL na última versão](https://www.postgresql.org/download/)
* psycopg2 (PostgreSQL Driver) : - pip install psycopg2

## 2. Instruções de construção, execução e uso da API

Antes de executar certifique-se de que o PostgreSQL está funcionando corretamente com o banco de dados com nome `meubanco` e com um usuário superuser com credenciais `orlando` e senha `orlando2552`.

A compilação execução do programa pode ser feita através do comando:

```
python programa.py
```

# 3. Escopo do produto

Sistema CRUD para PostgreSQL com Tkinter

# 3.1 Visão Geral
Um sistema CRUD (Create, Read, Update, Delete) com interface gráfica para gerenciar produtos em um banco de dados PostgreSQL. A interface gráfica é construída usando Tkinter, proporcionando uma maneira intuitiva de interagir com os dados do produto.

# 3.2 Requisitos Funcionais:

# 3.2.1 Conectar ao Banco de Dados:

Conectar automaticamente ao banco de dados PostgreSQL ao iniciar o aplicativo.

# 3.2.2 CRUD (Create, Read, Update, Delete):

Inserir novos produtos.
Atualizar produtos existentes.
Excluir produtos.
Buscar e visualizar detalhes do produto.

# 3.2.3 Interface Gráfica:

A interface deve ser fácil de usar, permitindo que o usuário realize operações CRUD através de uma GUI.

# 3.3 Requisitos Não Funcionais:

# 3.3.1 Usabilidade:

A aplicação deve ser fácil de usar e intuitiva.

# 3.3.2 Performance:

O sistema deve responder rapidamente às ações do usuário.

# 3.3.3 Feedback:

O sistema deve fornecer mensagens de feedback claras (sucesso/erro).

# 3.4 Casos de Uso:

# 3.4.1 Inserir Produto:

O usuário insere detalhes do produto, como ID, nome e preço.
O sistema valida as informações, insere o produto no banco de dados e mostra uma mensagem de sucesso.

# 3.4.2 Atualizar Produto:

O usuário seleciona um produto existente, modifica os detalhes e solicita a atualização.
O sistema valida as alterações, atualiza o produto no banco de dados e mostra uma mensagem de sucesso.

# 3.4.3 Excluir Produto:

O usuário seleciona um produto existente e solicita a exclusão.
O sistema remove o produto do banco de dados e mostra uma mensagem de sucesso.

# 3.4.4 Buscar Produto:

O usuário insere o ID do produto e solicita a busca.
O sistema recupera detalhes do produto do banco de dados e os exibe na interface.

# 3.4.5 Visualizar Produtos:

O sistema exibe todos os produtos existentes em uma tabela, incluindo ID, nome e preço, na inicialização e após cada operação CRUD.

# 3.4.6 Fluxo de Trabalho:

Ao iniciar, o sistema automaticamente se conecta ao banco de dados e carrega os produtos existentes.
O usuário pode então realizar operações CRUD, e o sistema exibirá mensagens de feedback apropriadas após cada operação.
Os detalhes dos produtos, como o preço acrescido em 10%, são calculados automaticamente pelo sistema durante as operações de inserção e atualização.

# 3.4.7 Considerações Adicionais:
O sistema inclui mensagens claras de erro e sucesso para informar o usuário sobre o resultado de cada operação.
A tabela de produtos é atualizada automaticamente para refletir qualquer modificação, garantindo que o usuário veja sempre os dados mais recentes.

# 4 Interface Gráfica

![TELA1](https://github.com/orlandoroxo/produtos-crud/blob/main/assets/tela1.png)
![TELA2](https://github.com/orlandoroxo/produtos-crud/blob/main/assets/tela2.png)
![TELA3](https://github.com/orlandoroxo/produtos-crud/blob/main/assets/tela3.png)
![TELA4](https://github.com/orlandoroxo/produtos-crud/blob/main/assets/tela4.png)
![TELA5](https://github.com/orlandoroxo/produtos-crud/blob/main/assets/tela5.png)

# 4 Registro no banco de dados

![BD](https://github.com/orlandoroxo/produtos-crud/blob/main/assets/bd.png)

