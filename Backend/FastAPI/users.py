from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Entidad User
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [
    User(id=1, name='Christian', surname='Arguello', url='https://arguedev.com', age=27),
    User(id=2, name='Moure', surname='Dev', url='https://mouredev.com', age=25),
    User(id=3, name='Brais', surname='Moure', url='https://braisdev.com', age=30),
    User(id=4, name='Miguel', surname='Angel', url='https://midudev.com', age=28),
]


@app.get('/usersjson')
async def usersjson():
    return [{'name': 'Christian', 'surname': 'Arguello', 'url': 'https://arguedev.com','age': 27},
        {'name': 'Moure', 'surname': 'Dev', 'url': 'https://mouredev.com','age': 25},
        {'name': 'Brais', 'surname': 'Moure', 'url': 'https://braisdev.com','age': 30},
        {'name': 'Miguel', 'surname': 'Angel', 'url': 'https://midudev.com', 'age': 28},]


@app.get('/usersclass')
async def usersclass():
    return users_list


@app.get("/users")
async def users():
    return users_list


# PATH
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# QUERY
@app.get("/usersquery/")
async def usersquery(id: int):
    return search_user(id)


# Funcion buscar user
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User not found"}