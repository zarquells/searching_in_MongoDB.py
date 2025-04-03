from pymongo import MongoClient
import json

# Conectar ao MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["data_movies"]

with open("mongoDB in Python/searching_data_mongoDB.py/data.json", "r", encoding="utf-8") as arquivo_json:
    series = json.load(arquivo_json)
    colecao_conteudos = db["conteudos"]  
    
    # Inserir todas as séries no banco de dados
    colecao_conteudos.insert_many(series)  

# Inserir o exemplo manual de Breaking Bad
novo_documento = {
    "Série": "Breaking Bad",
    "Ano de Lançamento": 2008,
    "Temporadas disponíveis": 5,
    "Linguagem": "Inglês",
    "Genero": ["Drama", "Crime"],
    "IMDb Avaliação": 9.5,
    "Classificação": "18+"
}

colecao_conteudos.insert_one(novo_documento)