from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()


@app.get('/')
def hello():
    return {'hello world'}

@app.post('/createposts')
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {'message': "successfully created posts"}