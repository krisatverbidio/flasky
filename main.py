from typing import Union, List
from pydantic import BaseModel
import subprocess
import uvicorn


from fastapi import FastAPI
import os

app = FastAPI()


class Command(BaseModel):
    command: List[str]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/run/")
def run_command(command: Command):
    r = subprocess.run(command.command, shell=True, capture_output=True)
    output = r.stdout.decode().splitlines()
    return output
    # return command

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")
