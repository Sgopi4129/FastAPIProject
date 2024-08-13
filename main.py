# from http.client import HTTPException
# from typing import Optional
# from fastapi import Depends
# from models import Base, User
# from pydantic import BaseModel
# from schema import UserSchema
# from database import engine,Sessionlocal
# from sqlalchemy.orm import Session
# from fastapi import FastAPI
#
# Base.metadata.create_all(bind=engine)
#
# def get_db():
#     try:
#         db = Sessionlocal()
#         yield db
#     finally:
#         db.close()
#
# app=FastAPI()
# @app.post("/adduser")
# def add_user(request:UserSchema, db: Session = Depends(get_db)):
#     user = User(name=request.name, email=request.email,nickname=request.nickname)
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user
#
# @app.get("/user/{user_id}")
# def get_users(user_id,db: Session= Depends(get_db)):
#     users = db.query(User).filter(User.id == user_id).first()
#     return users
#
# @app.delete("/delete/{id}")
# def delete(user_id: int, db:Session=Depends(get_db)):
#     db_user = db.query(User).filter(User.id == user_id).first()
#     if db_user:
#         db.delete(db_user)
#         db.commit()
#         return db_user
#     return f"users {user_id}doesn't exist"
#
# @app.put("/user/{user_id}")
# def update_user(user_id: int, request: UserSchema, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     user.name = request.name
#     user.email = request.email
#     user.nickname = request.nickname
#     db.commit()
#     db.refresh(user)
#     return user


import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

# app=FastAPI()
#
# class Item(BaseModel):
#     name:str
#     role:str
#     items={
#         "name":"harry",
#         "role":"software"
#     }
#
# @app.post("/items/{item_id}")
# def user_post(item_id:int|None,item:Item):
#     result={
#         "item_id":item_id,
#         "name":item.name,
#         "role":item.role
#     }
#     print("The method user_post() is working")
#
#     return result
# @app.get("/items/{item_id}")
# def user_id(item_id:int|None):
#     if item_id in Item.item_
#     results={"item_id":item_id}
#     print("The method user_id() is working on.....")
#     return results
