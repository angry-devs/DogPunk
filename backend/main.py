from fastapi import FastAPI
from pydantic import BaseModel


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
@app.get("/")
async def hello_world():
    return {"success": True, "message": "Hello World"}
@app.post("/items/")
async def create_item(item: Item):
    print(item)
    return item