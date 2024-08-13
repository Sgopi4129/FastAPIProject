# def get_full_name(first_name: str, last_name: str):
#     full_name = first_name.title() + " " + last_name.title()
#     return full_name


# print(get_full_name("john", "doe"))

# def get_fullname_with_age(name:str,age:int):
#     return f"{name}+is old age+{age}"
# print(get_fullname_with_age("ganesh",24))

# def process_items(items: list[str]):
#     for item in items:
#         print(item)

# print(process_items(["Ganesh","Aditya"]))

from fastapi import FastAPI,Query,Path
from pydantic import BaseModel
from typing import Annotated, Union

app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get")],
#     q: Annotated[str | None, Query(alias="item-query")] = None,
#     ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
# #     return results
#
# class Item(BaseModel):
#     name:str
#     description:str |None
#     price: float|None
#
# @app.post("/items/{item_id}")
# async def user_input(item_id:Annotated[str,Path(title="The id is required",gt=0,le=7)], item: Annotated[Item,Path(title="Item is required",gt=0,le=6)]):
#     results={"item_id":item_id,
#              "name":item.}
#     return results

# from fastapi import FastAPI,HTTPException
#
# app=FastAPI()
#
# items={
#         "name":"harry",
#         "role":"software"
#     }
#
# @app.post("/items/{item_id}")
# async  def put_user(item_id:str,item:items):
#     return items[item_id]
# @app.get("/items/{item_id}")
# async  def get_user(item_id:str):
#     if item_id not in items:
#         raise HTTPException(status_code=404,detail="Item not found")
#     return {"items":items[item_id]}
#
# from fastapi import FastAPI, HTTPException
#
# app = FastAPI()
#
# items = {"foo": "The Foo Wrestlers"}
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"item": items[item_id]}
#
# from fastapi import FastAPI, HTTPException
# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import PlainTextResponse
# from starlette.exceptions import HTTPException as StarletteHTTPException
#
# app = FastAPI()
#
#
# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
#
#
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
#     return {"item_id": item_id}

from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print(f"OMG! An HTTP error!: {repr(exc)}")
    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(f"OMG! The client sent invalid data!: {exc}")
    return await request_validation_exception_handler(request, exc)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}