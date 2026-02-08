from config.sql_config import get_sql
from fastapi import Fastapi
app=FastAPI()

@app.post("/create_user")
def create_user(name,email,password):
    db=get_sql()
    cursor=db.cursor(dictionary=True)
    cursor="insert into users (name,email,password) values (%s,%s,%s)"
    cursor.excute(query,(name,email,password))
    db.commit()
    cursor.close()
    db.close()
    return {"users": "created successfully"}  


@app.get("/login")
def get_user():
    db=get_sql()
    cursor=db.cursor(dictionary=True)
    query="INSERT INTO users (name,email,password) VALUES (%s,%s,%s)"
    cursor.excute(query,(name,email,password))
    db.commit()
    cursor.close()
    db.close()
    return {"users": "created successfully"}

