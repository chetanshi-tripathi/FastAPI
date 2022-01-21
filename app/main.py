
from typing import Optional, Any
from fastapi import FastAPI
from app.api.api import router as api_router
from mangum import Mangum

description="""
FAST API DEMO

## Features
1.
2.

## Additional Links
1.
2.
3.
4.
"""

app = FastAPI(title="Fast API Demo", description= description)



@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router, prefix="/api")
handler= Mangum(app)