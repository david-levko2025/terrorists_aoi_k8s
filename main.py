from fastapi import FastAPI, UploadFile
import uvicorn

app = FastAPI()


@app.post("/uploadfile")
def get_csv(file: UploadFile):
    return {"filename": file.filename} 




if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)