from fastapi import FastAPI
from app import config, db
from cassandra.cqlengine.management import sync_table
from app.users.models import User


app = FastAPI()
DB_SESSION = None

@app.on_event("startup")
def on_startup():
    # Triggered when fastapi starts
    print('Hello world')
    global DB_SESSION
    DB_SESSION = db.get_session()
    sync_table(User)

@app.get('/')
def home():
    return {"hello": "World"}