from flask import Flask, request
import psycopg2
import requests
import random
import time

app = Flask(__name__)

'''@app.route("/")
def home():
    return render_template("index.html")'''

def get_db_conn():
    conn = psycopg2.connect(
        host="db",
        database="projectTF",
        user="postgres",
        password="postgres"
    )
    return conn

def getSendData():  #GET method from pod GEN
    cont = 0
    while True:
        cont += 1
        print(f"\nciclo: {cont}")
        
        data = requests.get("http://data-gen:5000/data")
        if data.status_code == 200:
            data = data.json()
            
            cal = str(random.randint(6,10))  # random calification
            data["calificacion"] = cal  # append calification field to the data
            
            print("\nReceived enrollment request for Student: ", data["id"])
            print("Name: ", data["nombre"])
            print("Assignature: ", data["materia"])
            print("Cal: ", data["calificacion"], "\n")

            conn = get_db_conn()
            cur = conn.cursor()
            cur.execute("INSERT INTO students (id, name, assignature, cal) VALUES (%s, %s, %s, %s)", 
                        data["id"], (data["nombre"], data["materia"], data["calificacion"]))
            conn.commit()
            cur.close()
            conn.close()
        else:
            print("\nGet data failed. Server responded with status code:", data.status_code)

        time.sleep(5)


if __name__ == "__main__":
    getSendData()
    app.run(host="0.0.0.0", debug=False, port=5001)
