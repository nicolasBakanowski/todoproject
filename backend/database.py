from models.todomodel import Todo

#mongoDB driver 
import motor.motor_asyncio


conn_str = 'mongodb+srv://<user>:<pass>@cluster0.aw8wi.mongodb.net/<collection>?retryWrites=true&w=majority'
client = motor.motor_asyncio.AsyncIOMotorClient(conn_str)
database = client.TodoList
collection = database.todo


async def fetch_one_todo(title):
    document = await collection.find_one({"title":title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document 

async def update_todo(title, desc):
    await collection.update_one({"title":title},
    {"$set":{"description":desc}})
    document = await collection.find_one({"title":title})
    return document


async def remove_todo(title):
    await collection.delete_one({"title":title})
    return True   
