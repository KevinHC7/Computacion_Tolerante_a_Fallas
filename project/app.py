import requests
import psycopg2
from flask import Flask, request, render_template

app = Flask(__name__)

def get_db_conn():
    conn = psycopg2.connect(
        host="db",
        database="projectTF",
        user="postgres",
        password="postgres"
    )
    return conn


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_data")
def data():
    data = requests.get("http://data-gen:5000/data")

    if data.status_code == 200:
        print("\nWoohoo!, gathered successfully.")
        print(data)
        return "Cool", 200
    else:
        print(
            "\nFailed to enroll. Server responded with status code:", data.status_code)
        print("Response from server:", data.text)
        return "No data received.", 400


@app.route("/db_save", methods=["POST"])
def create():
    conn = get_db_conn()
    cur = conn.cursor()
    username = request.json.get("username")
    email = request.json.get("email")
    cur.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
    conn.commit()
    cur.close()
    conn.close()
    return "", 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
