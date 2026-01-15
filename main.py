from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
import pandas as pd
from service import Validation as valid
from db import Connection


app = FastAPI()

@app.post("/top-threats")
def create_file(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(detail="file not provided",status_code=400)
    top_terorists = valid(f'{file.filename}').top_5_terorists().to_dict(orient="dict")
    
    return { 
        "count":len(top_terorists),
         "top": [top_terorists] 
         }


if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)
