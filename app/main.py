import logging
import time
from pathlib import Path
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, ConfigDict, Field

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)
logger = logging.getLogger("wine-api")

app = FastAPI(
    title="Wine Quality Prediction API",
    version="1.0.0",
    description="MLOps inference service for wine quality scoring."
)

MODEL_PATH = Path(__file__).resolve().parent / "model.pkl"
if not MODEL_PATH.exists():
    MODEL_PATH = Path("app/model.pkl")

try:
    model = joblib.load(MODEL_PATH)
    logger.info(f"Random Forest model loaded successfully from {MODEL_PATH}.")
except Exception as e:
    logger.error(f"Failed to load model from {MODEL_PATH}: {e}")
    model = None

class WineFeatures(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    fixed_acidity: float = Field(..., json_schema_extra={"example": 7.4}, alias="fixed acidity")
    volatile_acidity: float = Field(..., json_schema_extra={"example": 0.7}, alias="volatile acidity")
    citric_acid: float = Field(..., json_schema_extra={"example": 0.0}, alias="citric acid")
    residual_sugar: float = Field(..., json_schema_extra={"example": 1.9}, alias="residual sugar")
    chlorides: float = Field(..., json_schema_extra={"example": 0.076}, alias="chlorides")
    free_sulfur_dioxide: float = Field(..., json_schema_extra={"example": 11.0}, alias="free sulfur dioxide")
    total_sulfur_dioxide: float = Field(..., json_schema_extra={"example": 34.0}, alias="total sulfur dioxide")
    density: float = Field(..., json_schema_extra={"example": 0.9978}, alias="density")
    pH: float = Field(..., json_schema_extra={"example": 3.51}, alias="pH")
    sulphates: float = Field(..., json_schema_extra={"example": 0.56}, alias="sulphates")
    alcohol: float = Field(..., json_schema_extra={"example": 9.4}, alias="alcohol")
    type_white: int = Field(..., json_schema_extra={"example": 0}, alias="type_white", description="1 for white, 0 for red")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"{request.method} {request.url.path} - Status: {response.status_code} - Latency: {duration:.4f}s")
    return response

@app.get("/health", status_code=200)
def health_check():
    if model is None:
        raise HTTPException(status_code=503, detail="Model artifact unavailable")
    return {"status": "healthy", "model_loaded": True}

@app.post("/predict")
def predict_quality(payload: WineFeatures):
    if model is None:
        raise HTTPException(status_code=503, detail="Model is not loaded.")

    try:
        input_data = pd.DataFrame([payload.model_dump(by_alias=True)])
        
        prediction = model.predict(input_data)
        logger.info(f"Input features: {payload.model_dump()} -> Prediction: {int(prediction[0])}")
        
        return {
            "predicted_quality": int(prediction[0]),
            "status": "success"
        }
    except Exception as e:
        logger.error(f"Inference error: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Inference failed: {str(e)}")