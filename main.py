from fastapi import FastAPI, UploadFile
import uvicorn
import pandas as pd
from service import ValidationOnData as valid
from db import Connection


app = FastAPI()


@app.post("/top-threats")
def get_the_csv_file(file: UploadFile):
    df = pd.read_csv(file.file)
    the_most_dangers_terrorists = df.sort_values(by = ["danger_rate"], ascending = False).head()
    dangers_terrorists_valid = valid.validating_terrorists(the_most_dangers_terrorists)
    result =Connection.insert_to_db(dangers_terrorists_valid)
    return {"count": len(dangers_terrorists_valid),
            "top": dangers_terrorists_valid}


if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)