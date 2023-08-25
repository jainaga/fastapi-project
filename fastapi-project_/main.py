from fastapi import FastAPI
from models import Todo


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

@app.get("/todos")
async def get_todos():
    return {"todos": todos}

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No se encontro el todo"}


@app.delete("/todos/{todo_id}")
async def del_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "borrado"}
    return {"message": "no se encontro todo"}

@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_object: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_object.id
            todo.title = todo_object.title
            return {"todo": todo} 
    return {"message": "No se encontro el todo para actualizar"}





@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created successfully"}
