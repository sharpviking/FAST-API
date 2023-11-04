from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    titleitle: str
    content: str


@app.get('/')
async def root():
    return {"message": "Welcome World!"}


@app.get("/posts")
def get_post():
    return {"data": "This is your post"}


@app.post("/createposts")
def create_post(new_post: Post):
    print(new_post.title)
    return {"data": "new post"}
