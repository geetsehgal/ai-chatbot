from fastapi import FastAPI

from routes.chat import router as chat_router
from routes.documents import router as doc_router

app = FastAPI()

app.include_router(chat_router)
app.include_router(doc_router)

@app.get("/")

def root():

    return {
        "status":"online"
    }
