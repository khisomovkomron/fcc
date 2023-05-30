from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None 


# request Get Method url: '/'
@app.get('/')
async def root():
    return {'message': "hello world"}

@app.get('/posts')
async def get_posts():
    return {'data':'This is your posts'}

@app.post('/createpost')
async def create_post(new_post: Post):
    print(new_post.published)
    print(new_post.dict())
    return new_post
