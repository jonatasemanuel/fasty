from fastapi import FastAPI

from routers import auth, users, todos

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}
