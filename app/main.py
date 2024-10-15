from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from IND service!"}

@app.get("/ind/")
async def root():
    return {"message": "No INDs yet"}
