from fastapi import FastAPI, Request
import controller

app = FastAPI()


@app.get('/london_houses')
async def london_houses(request: Request):
    return controller.get_london_houses(request=request)
