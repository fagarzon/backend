from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#crear entidad

class User(BaseModel):
    id: int
    name: str
    username: str
    url: str
    age: int

users_list = [User(id=1,name="Andre", username="fagar1", url="http:1", age=41),
           User(id=2,name="Felix", username="fagar2", url="http:2", age=42),
            User(id=3,name="Garzon", username="fagar3", url="http:3", age=43)]


@app.get("/usersjson")    
async def usersjson():
    return [{"name":"Andres","username":"fagar","url":"hhtp://","age":40},
            {"name":"Andres","username":"fagar","url":"hhtp://","age":40},
            {"name":"Andres","username":"fagar","url":"hhtp://","age":40}]
    
@app.get("/users")    
async def users():
    #return User(name="Andres",username="fagar",url="hhtp://",age=40)
    return users_list
# uvicorn users:app --reload

# Path
@app.get("/user/{id}")    
async def user(id: int):
    #return User(name="Andres",username="fagar",url="hhtp://",age=40)
    users = filter(lambda user: user.id == id,users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"no se han encontrado el usuario"}

# Query
@app.get("/user/")    
async def user(id: int):
    return search_user(id)
    #return User(name="Andres",username="fagar",url="hhtp://",age=40)
    #users = filter(lambda user: user.id == id,users_list)
    #try:
    #    return list(users)[0]
    #except:
    #    return {"error":"no se han encontrado el usuario"}


def search_user(id: int):
        users = filter(lambda user: user.id == id,users_list)
        try:
            return list(users)[0]
        except:
            return {"error":"no se han encontrado el usuario"}