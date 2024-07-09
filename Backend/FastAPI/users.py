from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad Usario
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = \
    [
        User(name='Christian', surname='Arguello', url='https://google.com/', age=26),
        User(name='Brais', surname='Moure', url='https://mouredev.com/', age=34),
        User(name='Haakon', surname='Dashleg', url='https://hakatoon.com/', age=23)
    ]

@app.get('/usersJson')
async def usersJson():
    return \
        [
            {'name': 'Christian', 'surname': 'Arguello', 'url': 'https://google.com/', 'age': 25},
            {'name': 'Brais', 'surname': 'Moure', 'url': 'https://mouredev.com/', 'age': 34},
            {'name': 'Haakon', 'surname': 'Dashleg', 'url': 'https://hakatoon.com/', 'age': 23},
        ]

@app.get('/users')
async def users():
    return users_list