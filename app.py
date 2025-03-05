from flask import Flask, jsonify
import psycopg2
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# PostgreSQL Connection
conn = psycopg2.connect(
    dbname="youtube_analysis",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

@app.route("/comments", methods=["GET"])
def get_comments():
    cursor.execute("SELECT * FROM youtube_comments")
    comments = cursor.fetchall()
    return jsonify(comments)

if __name__ == "__main__":
    app.run(debug=True)
