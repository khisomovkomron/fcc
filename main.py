from fastapi import FastAPI, Body, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None 

my_posts = [{'title': 'title of post 1', "content": 'content of post 1', 'id': 1},
             {'title': 'title of post 2', 'content': 'content of post 2', 'id': 2}]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i 
        
# request Get Method url: '/':
@app.get('/')
async def root():
    return {'message': "hello world"}

@app.get('/posts')
async def get_posts():
    return {'data': my_posts}

@app.post('/posts', status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000)

    my_posts.append(post_dict)
    return {'data': post_dict}

@app.get('/posts/{id}')
def get_post(id: int, response: Response):
    print(id)
    # return {'id': my_posts[id]}
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')
    return {'post_detail': post}

@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # deleting post
    # find index of a post in an array
    # my_posts.pop(idnex)

    index = find_index_post(id)
    my_posts.pop(index)

    return {'message': 'post was successfully deleted'}

last_episode = '2:05:48'