# 📌💡Gerenciador de Catálogos da Netflix com Azure Functions e Cosmos DB
Este projeto tem como objetivo construir uma API para gerenciar um catálogo de filmes e séries da Netflix. A API será implementada usando Azure Functions, que irá interagir com o Azure Cosmos DB para armazenar e gerenciar os dados.

## 🚀 Resumo
A aplicação irá realizar operações CRUD (Criar, Ler, Atualizar e Excluir) em um catálogo de filmes e séries. Utilizando Azure Functions como funções serverless e o Cosmos DB como banco de dados NoSQL, você terá uma solução altamente escalável e resiliente.

## 🛠️ Tecnologias Utilizadas 🌐
Azure Functions: Plataforma serverless para executar funções em resposta a eventos, como requisições HTTP.
Python: Linguagem de programação para implementar as funções.
Azure Cosmos DB: Banco de dados NoSQL com alta escalabilidade e baixo tempo de latência.
Visual Studio Code (VSCode): IDE para desenvolvimento.
Azure CLI: Ferramenta de linha de comando para interagir com o Azure.
## 🗂️ Estrutura do Projeto
A estrutura do projeto pode ser organizada da seguinte forma:

````
/gerenciador-catalogo-netflix
    /catalogo
        __init__.py          # Funções Azure para manipulação do catálogo
        cosmosdb.py          # Conexão e operações no Cosmos DB
        models.py            # Definição do modelo de dados (Filmes/Séries)
    /requirements.txt        # Dependências do Python
    /local.settings.json     # Configurações locais do Azure Functions (chaves, conexões)
    /function_app.py         # Função principal para as Azure Functions
    /README.md               # Documentação do projeto
````
## ⚙️ Passos para Implementação 
1. Configuração do Ambiente
a) Instalar o Python
Verifique se o Python 3.x esta instalado na sua máquina. Caso não tenha, faça o download e instalação através do site oficial do [Python](https://www.python.org/ftp/python/3.13.1/python-3.13.1-amd64.exe)

b) Instalar o Visual Studio Code (VSCode)
Se ainda não tiver o VSCode instalado, baixe-o aqui [Vscode](https://code.visualstudio.com/).

c) Instalar Extensões Necessárias no VSCode
Dentro do VSCode, instale as extensões:

- Python: Para suporte a código Python.
- Azure Functions: Para trabalhar com Azure Functions diretamente no VSCode.
- Azure CLI Tools: Para interagir com a Azure via linha de comando.
  
d) Instalar Azure Functions Core Tools
Instale o Azure Functions Core Tools para rodar e testar as funções localmente. No terminal, execute o seguinte comando:
```
npm install -g azure-functions-core-tools@4 --unsafe-perm true
````
e) Criar um Novo Projeto no Azure Functions
No terminal do VSCode, execute os seguintes comandos para criar um novo projeto de Azure Functions:
````
func init gerenciador-catalogo-netflix --python
cd gerenciador-catalogo-netflix
func new
````
