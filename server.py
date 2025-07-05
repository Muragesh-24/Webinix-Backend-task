from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scripts.db import Base, engine
import routes.routes

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(routes.routes.router)
