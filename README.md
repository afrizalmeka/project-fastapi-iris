# FastAPI Iris Prediction API

Simple FastAPI service for Iris prediction using a pickled scikit-learn KNeighborsClassifier.

## Requirements
- Python 3.10+

## Usage With Makefile
Build the virtual environment and install dependencies:

```bash
make build
```

Run the API server:

```bash
make run
```

You can also use:

```bash
make up
```

## Test With Swagger UI
After the server is running, open:

```
http://127.0.0.1:8000/docs
```

Use this JSON body in `/predict`:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Expected response:
```json
{"status":"success","prediction":0,"label":"Iris-setosa"}
```

Examples for each class:

Iris-setosa (0)
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Iris-versicolor (1)
```json
{
  "sepal_length": 6.0,
  "sepal_width": 2.9,
  "petal_length": 4.5,
  "petal_width": 1.5
}
```

Iris-virginica (3)
```json
{
  "sepal_length": 6.9,
  "sepal_width": 3.1,
  "petal_length": 5.4,
  "petal_width": 2.1
}
```

## Run Without Makefile
macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

## Model File
The API expects `model.pkl` in the project root. You can regenerate it with:

macOS/Linux:

```bash
.venv/bin/python train_model.py
```

Windows:

```powershell
.\.venv\Scripts\python train_model.py
```

The training data comes from `source_code/Iris-Classification-WebApp/Iris.csv`.
