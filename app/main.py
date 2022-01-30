
from typing import Optional, Any
from fastapi import FastAPI
from app.api.api import router as api_router
from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware
description="""
FastAPI- DynamoDB CRUD Operations

## Features
This project on FAST API contains 4 endpoints to perform CRUD operations on DynamoDB.
__________________________________________
    Name of DynamoDB Table= Employee
    Table consists of following fields:

            emp_id: str
            department: str
            emp_name: str
            designation: str
            emp_email: str
            emp_contact: str
__________________________________________

"""

app = FastAPI(title="Fast API Demo", description= description)
origins=[
    "*"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router, prefix="/api")
handler=Mangum(app)