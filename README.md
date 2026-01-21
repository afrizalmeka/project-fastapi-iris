# API Prediksi Iris dengan FastAPI

Layanan FastAPI sederhana untuk prediksi Iris menggunakan model scikit-learn (KNeighborsClassifier).

## Persyaratan
- Python 3.10+

## Penggunaan dengan Makefile
Catatan Windows:
- Makefile ini memakai shell POSIX (contoh: `. .venv/Scripts/activate`), jadi jalankan lewat WSL2 atau Git Bash/MSYS2, bukan PowerShell.
- Jika belum punya `make`, lihat panduan Windows di `README_Makefile.md`.
- Jika tidak ingin memasang `make`, gunakan langkah "Jalankan Tanpa Makefile" di bawah.

Bangun virtual environment dan install dependency:

```bash
make build
```

Jalankan server API:

```bash
make run
```

Alternatif:

```bash
make up
```

Hentikan server dengan `Ctrl+C`.

## Uji Dengan Swagger UI
Setelah server berjalan, buka:

```
http://127.0.0.1:8000/docs
```

Gunakan body JSON ini di `/predict`:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Contoh respons:
```json
{"status":"success","prediction":0,"label":"Iris-setosa"}
```

Contoh untuk setiap kelas:

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

Iris-virginica (2)
```json
{
  "sepal_length": 6.9,
  "sepal_width": 3.1,
  "petal_length": 5.4,
  "petal_width": 2.1
}
```

## Jalankan Tanpa Makefile
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

Hentikan server dengan `Ctrl+C`.

## File Model
API membutuhkan `model.pkl` di root project. Untuk membuat ulang:

macOS/Linux:

```bash
.venv/bin/python train_model.py
```

Windows:

```powershell
.\.venv\Scripts\python train_model.py
```

Data training diambil dari `source_code/Iris-Classification-WebApp/Iris.csv`.

## Dokumentasi API
Detail endpoint dan contoh request/response ada di [api.md](api.md).

## Dokumentasi Tambahan
- Panduan Makefile untuk pemula: [README_Makefile.md](README_Makefile.md)
- Referensi endpoint API: [api.md](api.md)
