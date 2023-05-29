from fastapi import FastAPI, Body


app = FastAPI()

# request Get Method url: '/'


@app.get('/')
async def root():
    return {'message': "hello world"}

@app.get('/posts')
async def get_posts():
    return {'data':'This is your posts'}

@app.post('/createpost')
async def create_post(payload: dict = Body(...)):
    print(payload)
    return {"message": f"title {payload['title']} content {payload['content']}"}
