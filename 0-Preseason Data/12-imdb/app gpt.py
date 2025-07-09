from flask import Flask, request, Response
import csv
import json

app = Flask(__name__)

# Charger les données une seule fois
movies = []
with open("imdb-movie-data.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movies.append(row)

# Route principale
@app.route('/', methods=['GET'])
def home():
    genre_param = request.args.get('genre')
    if genre_param:
        genre_lower = genre_param.lower()
        filtered = [
            movie for movie in movies
            if genre_lower in movie['Genre'].lower()
        ]
        return Response(json.dumps(filtered), content_type="application/json")
    return "Welcome to My IMDB API"

# Route dynamique pour les genres
@app.route('/<genre>', methods=['GET'])
def genre_filter(genre):
    genre_lower = genre.lower()
    filtered = [
        movie for movie in movies
        if genre_lower in movie['Genre'].lower()
    ]
    return Response(json.dumps(filtered), content_type="application/json")

if __name__ == '__main__':
    app.run(debug=True, port=8080)
