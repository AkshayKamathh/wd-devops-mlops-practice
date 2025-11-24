#!/usr/bin/env python3
from typing import List
from datetime import datetime

import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

MODEL_PATH = "model.pkl"
PREDICTION_LOG = "predictions.log"


class PredictRequest(BaseModel):
    features: List[float]  # 4 features for iris
        

app = FastAPI()
model = joblib.load(MODEL_PATH)


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": True}


@app.post("/predict")
def predict(req: PredictRequest):
    x = np.array(req.features).reshape(1, -1)
    pred = int(model.predict(x)[0])

    # Log prediction
    with open(PREDICTION_LOG, "a") as f:
        ts = datetime.utcnow().isoformat()
        f.write(f"{ts} prediction={pred}\n")

    return {"prediction": pred}
