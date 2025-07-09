Here’s a **clear explanation** of the Qwasar exercise **“My IMDB API”**, what it asks you to do, and how to approach it.

---

## 🎯 **Goal of the Project**

You need to create a **simple backend web API** that lets users **search for movies by genre** using a CSV file (like a mini-IMDB clone). The server must:

* Be written in **Python** (using **Flask**).
* Parse a given **CSV file** with movie data.
* Provide a **web interface** (API) to return filtered movies by genre.
* Serve on **port 8080**, and use **JSON** format for responses.

---

## 📂 **Project Setup**

### Required:

* A Python file: `app.py`
* A CSV file (provided by Qwasar)
* You can also create a `README.md` with instructions

---

## 🧪 **What Your App Must Do**

You must implement several **API endpoints** that allow users to get movies of a specific genre.

### 🔧 Routes to Implement:

| Route                                 | What It Does                                                                                           |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `/` + query param `?genre=`           | Filters by genre based on user input (case-insensitive). Example: `http://localhost:8080?genre=action` |
| `/action`                             | Returns all movies in genre Action                                                                     |
| `/adventure`                          | Returns all Adventure movies                                                                           |
| `/comedy`, `/drama`, `/romance`, etc. | Same for those genres                                                                                  |

Each route returns a list of movie dictionaries like:

```json
[
  {
    "Title": "Django Unchained",
    "Genre": "Drama,Western",
    "Year": "2012",
    ...
  },
  ...
]
```

---

## 📦 **What You Need to Do**

### 1. **Use Flask**

Install it with:

```bash
pip install flask
```

### 2. **Read the CSV File**

Parse it at the beginning, e.g., with `csv.DictReader`:

```python
import csv

with open("movies.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    movies = list(reader)
```

### 3. **Filter Movies by Genre**

Check if the genre is included in the `Genre` column (can contain multiple genres, separated by commas).

Example:

```python
def filter_movies_by_genre(genre):
    return [movie for movie in movies if genre.lower() in movie['Genre'].lower()]
```

### 4. **Create Routes in Flask**

Basic route with query parameter:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def genre_query():
    genre = request.args.get('genre')
    if genre:
        filtered = filter_movies_by_genre(genre)
        return jsonify(filtered)
    return jsonify([]), 204  # No content
```

Genre-specific route:

```python
@app.route('/action')
def action():
    return jsonify(filter_movies_by_genre('Action'))
```

Repeat for `/adventure`, `/comedy`, etc.

---

## ✅ **What You Must Ensure**

* The server **listens on `0.0.0.0`**, **port 8080**
* Responses are in **JSON format**
* Your filtering should be **case-insensitive**
* Your app should **not crash** if genre is missing

---

## 💻 **How to Run**

In your README, explain something like:

```bash
pip install flask
python app.py
```

Then access it in your browser or using `curl`:

```bash
curl "http://localhost:8080?genre=drama"
curl "http://localhost:8080/comedy"
```

If on `docode`, your server will be at:

```
http://web-XXXXXXXX.docode.YYYY.qwasar.io
```

---

## 🧠 **What You Learn**

* Basics of a **REST API**
* How to use **Flask** (light Python web framework)
* How to work with **CSV files**
* How to **filter data** and **serve JSON responses**
* The idea of **HTTP routes**, **GET methods**, and **status codes**

---

Would you like a template code to get started?
