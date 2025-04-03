from pymongo import MongoClient
import gridfs

client = MongoClient('mongodb://localhost:27017/')
db     = client['data_movies']
coll   = db['conteudos']
fs = gridfs.GridFS(db)

# Qual comando você usaria para encontrar todas as séries que estão em inglês
# english_series = coll.find({},{'Linguagem': 'Inglês'})
# print(*english_series, sep=', \n')

# Liste todas as séries lançadas a partir de 2018
# series_2018 = coll.find({},{'Ano de Lançamento': '2018'})
# print(*series_2018, sep=', \n')

# Quantas séries da base de dados possuem a classificação '18+'
# series_more18 = coll.count_documents({'Classificação': '18+'})
# print(series_more18)

# Liste todas as séries que pertencem ao gênero 'Ficção científica'
# series_scifi= coll.find({},{'Genero': 'Ficção científica'})
# print(*series_scifi, sep=', \n')

# Escreva um comando para exibir as séries ordenadas pela avaliação do IMDb, da maior para a menor
series_IMDB= coll.find.sort({},{'Classificação': '+18'})
print(*series_IMDB, sep=', \n')

# Atualize a série "The Boys" para adicionar mais uma temporada, passando de 2 para 3

# Escreva um comando para remover a série 'Suits' da base de dados

# Retorne apenas o nome e o ano de lançamento de todas as séries, ocultando os outros campos

# Liste todas as séries com IMDb Avaliação maior que 8.0