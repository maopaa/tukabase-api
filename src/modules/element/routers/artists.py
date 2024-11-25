
from fastapi import APIRouter

router = APIRouter(
    prefix = "/artist",
    tags = [ "Artist" ],
    responses = { 404: { "message": "No encontrado.", "description": "" } }
)

@router.get("/all")
async def getAllArtists():
    return [ "Artist 1", "Artist 2", "Artist 3" ]