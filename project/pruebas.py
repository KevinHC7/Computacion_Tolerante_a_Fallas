import random
import json

if __name__ == "__main__":
    name = ["Juan", "María", "Luis", "Ana", "Carlos"]
    assignature = ["Matemáticas", "Ciencias", "Historia", "Literatura", "Inglés"]

    data = {}
    data["id"] = random.randint(1000, 10000)  # random calification between 6-10
    data["nombre"]  = random.choice(name)
    data["materia"] = random.choice(assignature)
    print(type(data))
    print(data)
    
    print("\nReceived enrollment request for Student: ", data["id"])
    print("Name: ", data["nombre"])
    print("Assignature: ", data["materia"])

    data = data.json()
    print(type(data))
    print(data)
