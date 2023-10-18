""" 
    Cette fonction est le point d'entrée de programme d'API.
"""

# Import de la bibliothéque nécessaire.

from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def root():
    return {
        "message": "Welcome to MLops_Data !!"
    }