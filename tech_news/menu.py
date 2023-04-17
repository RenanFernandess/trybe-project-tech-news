from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.scraper import get_tech_news
import sys


# Requisitos 11 e 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    messages = (
        "Digite quantas notícias serão buscadas:\n",
        "Digite o título:\n",
        "Digite a data no formato aaaa-mm-dd:\n",
        "Digite a categoria:\n",
    )

    response = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair."
    )

    match response:
        case "0":
            return get_tech_news(int(input(messages[0])))
        case "1":
            return search_by_title(input(messages[1]))
        case "2":
            return search_by_date(input(messages[2]))
        case "3":
            return search_by_category(input(messages[3]))
        case "4":
            return top_5_categories()
        case "5":
            return print("Encerrando script")
        case _:
            return sys.stderr.write("Opção inválida\n")
