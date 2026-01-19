from fastapi import Body, FastAPI
import pickle

app = FastAPI()

model = pickle.load(open("model.pkl", "rb"))


@app.post("/predict")
def predict_data(
    sepal_length: float = Body(..., description="Sepal length (cm)", example=5.1),
    sepal_width: float = Body(..., description="Sepal width (cm)", example=3.5),
    petal_length: float = Body(..., description="Petal length (cm)", example=1.4),
    petal_width: float = Body(..., description="Petal width (cm)", example=0.2),
):
    features = [sepal_length, sepal_width, petal_length, petal_width]
    prediction = model.predict([features])
    pred_id = int(prediction[0])
    label_map = {
        0: "Iris-setosa",
        1: "Iris-versicolor",
        3: "Iris-virginica",
    }
    return {
        "status": "success",
        "prediction": pred_id,
        "label": label_map.get(pred_id, "unknown"),
    }
