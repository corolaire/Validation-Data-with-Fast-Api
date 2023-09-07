from fastapi import APIRouter,Path,Query
from models.profile import profile
from models.user import user #models.user entra al archivo user dentro de la carpeta models e importa la clase user.

router=APIRouter()

@router.get('/profile/{id}')
def get_profile(id:str):
    return profile

@router.post('/profile/{}')
def post_profile():
    pass
@router.put('/profile/{}')
def put_profile():    
    pass
@router.delete('/profile/{id}')
def delete_profile(id:str):
    pass