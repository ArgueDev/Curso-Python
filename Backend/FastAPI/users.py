from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Entidad User
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int


users = [
    User(name='Christian', surname='Arguello', url='https://arguedev.com', age=27),
    User(name='Moure', surname='Dev', url='https://mouredev.com', age=25),
    User(name='Brais', surname='Moure', url='https://braisdev.com', age=30),
    User(name='Miguel', surname='Angel', url='https://midudev.com', age=28),
],

@app.get('/usersjson')
async def usersjson():
    return [
        {
            'name': 'Christian', 
            'surname': 'Arguello', 
            'url': 'https://arguedev.com',
            'age': 27
        },
        {
            'name': 'Moure', 
            'surname': 'Dev', 
            'url': 'https://mouredev.com',
            'age': 25
        },
        {
            'name': 'Brais', 
            'surname': 'Moure', 
            'url': 'https://braisdev.com',
            'age': 30
        },
        {
            'name': 'Miguel', 
            'surname': 'Angel', 
            'url': 'https://midudev.com',
            'age': 28
        },
    ]


@app.get('/usersclass')
async def usersclass():
    return users