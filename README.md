<a name="readme-top"></a>
# :construction: README customizado em construção ! :construction:
<!-- Olá, Tryber!
Esse é apenas um arquivo inicial para o README do seu projeto no qual você pode customizar e reutilizar todas as vezes que for executar o trybe-publisher.

Para deixá-lo com a sua cara, basta alterar o seguinte arquivo da sua máquina: ~/.student-repo-publisher/custom/_NEW_README.md

É essencial que você preencha esse documento por conta própria, ok?
Não deixe de usar nossas dicas de escrita de README de projetos, e deixe sua criatividade brilhar!
:warning: IMPORTANTE: você precisa deixar nítido:
- quais arquivos/pastas foram desenvolvidos por você; 
- quais arquivos/pastas foram desenvolvidos por outra pessoa estudante;
- quais arquivos/pastas foram desenvolvidos pela Trybe.

* Utilizar o terminal interativo do Python.
   * Utilizar estruturas condicionais e de repetição.
   * Utilizar funções built-in do Python.
   * Utilizar tratamento de exceções.
   * Realizar a manipulação de arquivos.
   * Escrever funções.
   * Escrever testes com Pytest.
   * Escrever seus próprios módulos e importá-los em outros códigos.
-->

# Tech News

<details>
  <summary>Índice</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o Projeto</a>
      <ul>
        <li><a href="#construido-com">Construido Com</a></li>
      </ul>
    </li>
    <li>
      <a href="#começando">Começando</a>
      <ul>
        <li><a href="#instalação">Instalação</a></li>
        <li><a href="#ambiente-virtual">Ambiente virtual</a></li>
        <li><a href="#tests">Tests</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#contato">Contato</a></li>
    <li><a href="#agradecimentos">Agradecimentos</a></li>
  </ol>
</details>

## Sobre o Projeto

O projeto tem como principal objetivo fazer consultas em notícias sobre tecnologia, através de raspagem de dados(web-scraping).

> As notícias podem ser obtidas através da raspagem do [blog da Trybe](https://blog.betrybe.com/).

### Habilidades trabalhadas

* Utilizar o terminal interativo do Python
* Escrever seus próprios módulos e importá-los em outros códigos
* Aplicar técnicas de raspagem de dados
* Extrair dados de conteúdo HTML
* Armazenar os dados obtidos em um banco de dados

### Construido Com

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![pytest](https://img.shields.io/badge/pytest-3670A0?style=for-the-badge&logo=pytest&logoColor=ffdd54)
* ![parsel](https://img.shields.io/badge/parsel-%23000.svg?style=for-the-badge&logo=parsel&logoColor=white)
* ![requests](https://img.shields.io/badge/requests-white.svg?style=for-the-badge&logo=requests&logoColor=black)
* ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
* ![pymongo](https://img.shields.io/badge/pymongo-3670A0?style=for-the-badge&logo=pymongo&logoColor=ffdd54)

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Começando

### Instalação

1. Clonar o repositorio

        git clone git@github.com:RenanFernandess/trybe-project-tech-news.git

2. Entrar na pasta project-job-insights

        cd ./trybe-project-tech-news

### Banco de dados

1. Rodar MongoDB via Docker:

        docker-compose up -d mongodb

### Docker

    ...

### Ambiente virtual

O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

1. **criar o ambiente virtual**

        python3 -m venv .venv

2. **ativar o ambiente virtual**

        source .venv/bin/activate

3. **instalar as dependências no ambiente virtual**

        python3 -m pip install -r dev-requirements.txt

> Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

### Tests

 Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

    python3 -m pytest

  <details>
  <summary>Mais comandos</summary>
  
   O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```

</details>

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Uso

1. Abra um terminal Python importando as funções do arquivo menu.py

        python3 -i tech_news/menu.py

2. Executar a função analyzer_menu()

        analyzer_menu()

> Após executar a função `analyzer_menu()` vai aparecer a seguinte mensagem no seu terminal.
```
 Selecione uma das opções a seguir:
  0 - Popular o banco com notícias;
  1 - Buscar notícias por título;
  2 - Buscar notícias por data;
  3 - Buscar notícias por categoria;
  4 - Listar top 5 categorias;
  5 - Sair.
```

3. Digite o número da opção para selecioná-la.
    1. Após selecionar `Popular o banco com notícias`, digite quantas notícias serão buscadas.
        > O banco de dados será populado com a quantidade de notícias informada.

    2. Após selecionar `Buscar notícias por título`, digite o título.

        Ao buscar pelo título "Frameworks de", será retornada uma lista de tuplas contendo o título e URL da notícia com título correspondente:

                [('Frameworks de programação', 'https://blog.betrybe.com/novidades/noticia_9.htm')]

        > A busca por título é `case insensitive`, ou seja, se não é obrigatório digitar letras maiúsculas; também não é necessário digitar o título completo.

    3. Após selecionar `Buscar notícias por data`, digite a data no formato aaaa-mm-dd(ano-mês-dia).

        Ao buscar pela data "2020-11-23", será retornada uma lista de tuplas contendo o título e URL da notícia com título correspondente:

                [('Frameworks de programação', 'https://blog.betrybe.com/novidades/noticia_9.htm')]

    4. Após selecionar `Buscar notícias por categoria`, digite a categoria.

        Ao buscar pela categoria "tecnologia", será retornada uma lista de tuplas contendo o título e URL da notícia com título correspondente:

                [('Frameworks de programação', 'https://blog.betrybe.com/novidades/noticia_9.htm')]

        > A busca por categoria é `case insensitive`, ou seja, se não é obrigatório digitar letras maiúsculas

    5. Após selecionar `Listar top 5 categorias`, será retornada uma lista com as 5 categorias mais encontradas.

          Retorno: ```['Tecnologia', 'Carreira', 'Ferramentas', 'Desenvolvimento Web', 'Desenvolvimento web']```

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Contato

* Renan Fernandes - [Linkedin](https://www.linkedin.com/in/orenanfernandes/) - renzinestuods@gmail.com

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Agradecimentos

* [Trybe](https://www.betrybe.com/)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
