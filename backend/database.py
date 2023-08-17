from model import Todo
from motor import motor_asyncio

# Connect to mongodb database
client = motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

# Create database and collection (table)
database = client.TodoList
collection = database.todo


# Get document by title
async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({}) # mongodb method
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document) # mongodb method
    return document

async def update_todo(title, desc):
    await collection.update_one({"title": title}, {"$set": {"description": desc}}) # mongodb method
    document = await collection.find_one({"title": title}) # retrieve updated document
    return document

async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True

