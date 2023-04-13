from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from unittest.mock import MagicMock
import pytest


@pytest.fixture
def news():
    return [
        {
            "url": "https://blog.betrybe.com/tecnologia/cabos-de-rede/",
            "title": (
                "Cabos de rede: o que são, quais os tipos e como crimpar?"
            ),
            "timestamp": "10/04/2023",
            "writer": "Dayane Arena dos Santos",
            "reading_time": 9,
            "summary": "Os cabos de rede são itens extremamente necessários",
            "category": "Tecnologia",
        },
        {
            "url": (
                "https://blog.betrybe.com/desenvolvimento-web/estruturas-de-"
                "repeticao/"
            ),
            "title": (
                "Estruturas de repetição: quais as 4 principais e quando "
                "usá-las?"
            ),
            "timestamp": "05/04/2023",
            "writer": "Vinicius Martins",
            "reading_time": 5,
            "summary": "As estruturas de repetição estão muito presentes na",
            "category": "Desenvolvimento Web",
        },
        {
            "url": "https://blog.betrybe.com/tecnologia/website-development/",
            "title": (
                "Website development: o que é, o que faz e salário! O guia "
                "inicial!"
            ),
            "timestamp": "31/03/2023",
            "writer": "Lucas Custódio",
            "reading_time": 13,
            "summary": "O Website development pode ser encontrado no mercado",
            "category": "Tecnologia",
        },
        {
            "url": "https://blog.betrybe.com/tecnologia/code-review/",
            "title": "Code Review: como virar um caçador de bugs com 15 dicas",
            "timestamp": "22/03/2023",
            "writer": "Cairo Noleto",
            "reading_time": 20,
            "summary": "Manter a consistência do código de um projeto",
            "category": "Tecnologia",
        },
    ]


def test_reading_plan_group_news(news):
    ReadingPlanService._db_news_proxy = MagicMock(return_value=news)

    message = "Valor 'available_time' deve ser maior que zero"
    with pytest.raises(ValueError, match=message):
        ReadingPlanService.group_news_for_available_time(available_time=0)

    result = ReadingPlanService.group_news_for_available_time(14)
    readable = result["readable"]

    assert len(readable) == 3
    assert readable[0]["unfilled_time"] == 5
    assert len(readable[0]["chosen_news"]) == 1
    assert readable[1]["unfilled_time"] == 9
    assert len(readable[1]["chosen_news"]) == 1
    assert len(result["unreadable"]) == 1
