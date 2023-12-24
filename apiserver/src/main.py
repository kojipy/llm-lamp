import logging

from fastapi import FastAPI
from pydantic import BaseModel


class PredictItem(BaseModel):
    word: str


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
async def predict(predict_item: PredictItem):
    logging.info(f"predict_item : {predict_item}")
    return {"embedding": [1.0, -0.5, 0.01]}
