from fastapi import FastAPI
import pickle
import numpy as np


# Load the trained model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)


# Initialize FastAPI app
app = FastAPI()


@app.get('/')
def home():
    return {"message": "Welcome to the Iris Classifier API!"}


@app.post("/predict/")
def predict(features: list):
    """
    Accepts a list of 4 numerical features and returns the predicted class.
    Example input: {"features": [5.1, 3.5, 1.4, 0.2]}
    """
    try:
        prediction = model.predict([np.array(features)])[0]
        return {"prediction": int(prediction)}
    except Exception as e:
        return {"error": str(e)}
