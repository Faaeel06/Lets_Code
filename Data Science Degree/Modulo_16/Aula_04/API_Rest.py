from fastapi import FastAPI
from pydantic import BaseModel
import requests

# univcorn api:app --reload --port 8001

class User(BaseModel):
    nome: str
    idade: int

users = [
         {"Nome":"Rafael", "Idade":28},
         {"Nome":"Joyce", "Idade":26},
         {"Nome":"Gilberto", "Idade":32},
         {"Nome":"Manu", "Idade":9},
         {"Nome":"João Lucas", "Idade":20},
         {"Nome": "Maria Aparecida", "Idade":48},
         {"Nome": "Maria Salete", "Idade":70}
         ]

app = FastAPI()

@app.get("/status")
def status() -> dict:
    return {"status": "on"}

@app.get("/users")
def get_users() -> list:
    return users

@app.get("/users/{index}")
def get_user_index(index:int) -> dict:
    return users[index]

@app.post("/users")
def Create_user(user: User):
    users.append(user)
    return {"msg":"Usuário cadastrado!"}

@app.put("/users/{index}")
def update_user(index:int, user:User):
    users[index] = user
    return {"msg": "Usuário atualizado!"}

@app.delete("/users/{index}")
def remove_user(index:int):
    users.pop(index)
    return {"msg": "Usuário apagado!"}

@app.get("/experiments")
def get_experiments():
    url = ''
    response = requests.request('GET', url=url)
    dados = response.json()
    return dados
    