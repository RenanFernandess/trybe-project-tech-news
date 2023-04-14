# Requisito 10
from tech_news.database import db


def top_5_categories():
    """Seu código deve vir aqui"""
    pepelines = [
        {
            "$group": {
                "_id": "$category",
                "count": {"$sum": 1},
            }
        },
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ]
    return [item["_id"] for item in db.news.aggregate(pepelines)]
