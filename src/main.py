from fastapi import FastAPI

app = FastAPI()

# Importing the routers
from src.modules.element.routers import artists

# Declaring the routers
app.include_router(artists.router)
