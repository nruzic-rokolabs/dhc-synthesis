from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from SOW Service!"}

@app.get("/sow/")
async def root():
    return {"message": "No SOWs at the moment!"}
