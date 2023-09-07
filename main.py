from fastapi import FastAPI,Query,Path
from models.profile  import profile
from models.user import user
from database import conn 
from routers import userrouter,profilerouter

app=FastAPI()

app.include_router(userrouter.router)
app.include_router(profilerouter.router)

@app.get('/')
def message():
    return 'welcome to my page Validation Data With Fast Api'

if __name__=='__main__':
    import uvicorn
    uvicorn.run(app,port=8000)