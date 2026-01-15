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

    # df = pd.read_csv(file.filename)
    # # the_most_dangers_terrorists = df.sort_values(by = ["danger_rate"], ascending = False).head()
    # dangers_terrorists_valid = valid.validation_data()
    # result =Connection.insert_to_db(dangers_terrorists_valid)
    # return {"count": len(dangers_terrorists_valid),
    #         "top": dangers_terrorists_valid}