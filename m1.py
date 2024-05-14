from fastapi import FastAPI

str = "added to check feature branch" 
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}