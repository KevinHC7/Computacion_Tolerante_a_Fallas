from flask import Flask, render_template
import random

app = Flask(__name__)
name = ["Juan", "María", "Luis", "Ana", "Carlos"]
assignature = ["Matemáticas", "Ciencias", "Historia", "Literatura", "Inglés"]


@app.route("/data")  #send data to DISP
def data():
    data = {}
    data["id"] =      str(random.randint(1000, 10000))  # random calification between 6-10
    data["nombre"] =  random.choice(name)
    data["materia"] = random.choice(assignature)
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
