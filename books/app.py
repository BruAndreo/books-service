from fastapi import FastAPI


app = FastAPI(title="Books Service")


@app.get("/")
def echo():
    return {"message": "Hello Books Service"}


@app.on_event("startup")
def on_startup():
    print("Books service is starting")


@app.on_event("shutdown")
def on_shutdown():
    print("Books service is shutting down")
