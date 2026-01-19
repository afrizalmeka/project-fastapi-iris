# Dokumentasi API

Base URL:

```
http://127.0.0.1:8000
```

Swagger UI:

```
/docs
```

Redoc:

```
/redoc
```

## POST /predict
Memprediksi jenis Iris berdasarkan 4 fitur.

Content-Type: `application/json`

Request body:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Field:
- `sepal_length` (float): panjang sepal dalam cm
- `sepal_width` (float): lebar sepal dalam cm
- `petal_length` (float): panjang petal dalam cm
- `petal_width` (float): lebar petal dalam cm

Response 200:

```json
{
  "status": "success",
  "prediction": 0,
  "label": "Iris-setosa"
}
```

Mapping kelas:
- `0` -> `Iris-setosa`
- `1` -> `Iris-versicolor`
- `3` -> `Iris-virginica`

Contoh curl:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
```

Catatan:
- Jika field kurang atau tipe data salah, FastAPI akan mengembalikan `422 Unprocessable Entity`.
