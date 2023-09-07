from fastapi import APIRouter,Path,Query
from models.profile import profile
from models.user import user

router=APIRouter()

@router.get('/user/{}')
def get_user():
   pass 
@router.post('/user/{}')
def post_user():
   pass 
@router.delete('/user/{}')
def delete_user():
    pass
