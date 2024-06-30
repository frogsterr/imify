from fastapi import FastAPI
from pydantic import BaseModel
import requests

class userInput(BaseModel):
    prompt: str

app = FastAPI()


@app.get("/")
def home():
    return "Hello World!"

#Handles user query
@app.get("/query")
def search(user_input: userInput):
    prompt = userInput.prompt
    
    if prompt is None:
        raise requests.HTTPError()
    
    
