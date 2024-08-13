# from typing import List, Optional
# from pydantic import BaseModel
# from fastapi import FastAPI, HTTPException
#
# import uuid
#
# app = FastAPI()
#
# # Define a Pydantic model for Item
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#
# # In-memory database
# items_db = []
#
# # CRUD operations
#
# # Create operation
# @app.post("/items/", response_model=Item)
# def create_item(item: Item):
#     item.id = str(uuid.uuid4())
#     items_db.append(item)
#     return item
#
# # Read operation (get all items)
# @app.get("/items/", response_model=List[Item])
# def read_items():
#     return items_db
#
# # Read operation (get single item by ID)
# @app.get("/items/{item_id}", response_model=Item)
# def read_item(item_id: str):
#     for item in items_db:
#         if item.id == item_id:
#             return item
#     raise HTTPException(status_code=404, detail="Item not found")
#
# # Update operation
# @app.put("/items/{item_id}", response_model=Item)
# def update_item(item_id: str, item: Item):
#     for i in range(len(items_db)):
#         if items_db[i].id == item_id:
#             items_db[i] = item
#             return item
#     raise HTTPException(status_code=404, detail="Item not found")
#
# # Delete operation
# @app.delete("/items/{item_id}", response_model=Item)
# def delete_item(item_id: str):
#     for i in range(len(items_db)):
#         if items_db[i].id == item_id:
#             deleted_item = items_db.pop(i)
#             return deleted_item
#     raise HTTPException(status_code=404, detail="Item not found")
#
# # Run the application with uvicorn
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8000)
