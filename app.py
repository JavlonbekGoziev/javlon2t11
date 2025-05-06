from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# PostgreSQL bazasiga ulanish
conn = psycopg2.connect(
    host="javlon2t.ct6ei6agkus4.ap-south-1.rds.amazonaws.com",
    database="db_javlonbek",
    user="postgres",
    password="postgres"
)

@app.route('/movies', methods=['GET'])
def get_movies():
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies;")
    movies = cur.fetchall()
    cur.close()

    # JSON formatida ma'lumot yuborish
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def add_movie():
    title = request.json.get('title')
	 genre = request.json.get('genre')
    release_year = request.json.get('release_year')

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO movies (title, genre, release_year) VALUES (%s, %s, %s)",
        (title, genre, release_year)
    )
    conn.commit()
    cur.close()

    return jsonify({'message': 'Movie added successfully!'}), 201

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM movies WHERE id = %s", (movie_id,))
    conn.commit()
    cur.close()

    return jsonify({'message': 'Movie deleted successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
