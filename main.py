from fastapi import FastAPI
from routers import category

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "My shop"}

app.include_router(category.router) # позволит подкл.доп.внешн.роутеры и маштабировать приложение



