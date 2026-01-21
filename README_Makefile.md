# Panduan Makefile untuk Menjalankan Aplikasi Iris API

Dokumen ini menjelaskan dua cara menjalankan aplikasi:
1) Tanpa Makefile (manual). Cocok jika kamu belum punya `make` di komputer.
2) Dengan Makefile. Lebih cepat, konsisten, dan minim salah ketik.

Tujuan utama: membantu pemula memahami langkah yang terjadi di balik perintah, bukan hanya menyalin perintahnya.

---

## Konsep singkat: apa itu Makefile?
Makefile adalah file berisi kumpulan "shortcut" untuk menjalankan perintah-perintah yang sering dipakai.
Di project ini, Makefile dipakai untuk:
- membuat virtual environment,
- menginstal dependency,
- menjalankan server FastAPI.

Hasilnya: lebih rapi, cepat, dan kecil risiko salah perintah.

---

## Tanpa Makefile (manual)
Ini adalah cara "manual" yang setara dengan apa yang dilakukan Makefile.
Kelebihan: tidak butuh `make`.
Kekurangan: lebih banyak langkah, rawan salah ketik.

### Tujuan tiap langkah
1. Membuat virtual environment
   - Tujuan: memisahkan dependency project dari Python global.
   - Alasan: supaya tidak bentrok dengan project lain.

2. Mengaktifkan virtual environment
   - Tujuan: memastikan `pip install` masuk ke environment yang benar.

3. Instal dependency
   - Tujuan: memasang semua library yang dibutuhkan API.

4. Menjalankan server
   - Tujuan: menyalakan FastAPI agar bisa diakses di browser.

### Langkah manual macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Langkah manual Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

Hentikan server dengan `Ctrl+C`.

---

## Dengan Makefile
Ini cara yang lebih ringkas. Kamu cukup mengingat beberapa perintah.

### Prasyarat
- Python 3.10+
- `make` terpasang
  - macOS/Linux: biasanya sudah ada.
  - Windows: gunakan WSL2 atau Git Bash/MSYS2. Lihat bagian "Windows: instalasi make" di bawah.

### Windows: instalasi make
Makefile ini memakai shell POSIX (contoh: `. .venv/Scripts/activate`), jadi jalankan `make` dari WSL2 atau Git Bash/MSYS2. Jika tetap di PowerShell, gunakan langkah manual di atas.

#### Opsi 1: WSL2 (disarankan)
1. Install WSL2 (PowerShell Admin):
   ```powershell
   wsl --install
   ```
2. Buka terminal Ubuntu/WSL, lalu install make:
   ```bash
   sudo apt update && sudo apt install -y make
   ```
3. Masuk ke folder project dari WSL (contoh):
   ```bash
   cd /mnt/c/Users/<nama>/path/project-fastapi-iris
   ```
4. Jalankan:
   ```bash
   make build
   make run
   ```

#### Opsi 2: Git Bash atau MSYS2 (tanpa WSL)
1. Install Git for Windows (Git Bash) atau MSYS2.
2. Install `make` (pilih salah satu):
   - Scoop: `scoop install make`
   - Chocolatey: `choco install make`
   - MSYS2: `pacman -S make`
3. Buka Git Bash/MSYS2 di folder project, lalu cek:
   ```bash
   make --version
   ```

### Perintah yang tersedia
Di bawah ini ada dua bagian:
1) Isi Makefile agar kamu tahu persis perintah yang dijalankan.
2) Penjelasan detail tiap perintah `make`.

### Isi Makefile (ringkas)
```makefile
VENV_DIR ?= .venv

ifeq ($(OS),Windows_NT)
PYTHON ?= python
VENV_BIN := $(VENV_DIR)/Scripts
else
PYTHON ?= python3
VENV_BIN := $(VENV_DIR)/bin
endif

ACTIVATE := . $(VENV_BIN)/activate

.PHONY: build run up

build:
	$(PYTHON) -m venv --clear $(VENV_DIR)
	$(ACTIVATE) && pip install -r requirements.txt

run: up

up:
	$(ACTIVATE) && uvicorn main:app --reload
```

### Penjelasan bagian-bagian Makefile
- `VENV_DIR ?= .venv` menetapkan lokasi virtual environment. Bisa diubah saat menjalankan make, contoh: `make VENV_DIR=.venv2 build`.
- Blok `ifeq ($(OS),Windows_NT)` memilih:
  - `PYTHON` (Windows: `python`, macOS/Linux: `python3`)
  - `VENV_BIN` (Windows: `.venv/Scripts`, macOS/Linux: `.venv/bin`)
- `ACTIVATE := . $(VENV_BIN)/activate` adalah perintah untuk mengaktifkan virtual environment di shell yang dipakai `make`.
- `.PHONY` memastikan `make build`, `make run`, `make up` selalu dijalankan walau ada file bernama sama.

#### `make build`
Melakukan 2 hal secara berurutan:
1) Membuat ulang virtual environment di `.venv`
   - macOS/Linux: `python3 -m venv --clear .venv`
   - Windows: `python -m venv --clear .venv`
2) Mengaktifkan environment lalu instal dependency:
   - macOS/Linux: `. .venv/bin/activate && pip install -r requirements.txt`
   - Windows: `. .venv/Scripts/activate && pip install -r requirements.txt`

Catatan: opsi `--clear` akan menghapus isi `.venv` lama, jadi package lama ikut hilang.
Ini bagus untuk memastikan environment bersih dan konsisten.
Tambahan: setiap baris perintah di Makefile berjalan di shell terpisah, jadi aktivasi dibuat dalam satu baris yang sama dengan `pip` menggunakan `&&`.

#### `make run`
Menjalankan target `up`. Artinya `make run` dan `make up` hasilnya sama.
Ini dibuat supaya pengguna punya dua nama perintah yang mudah diingat.

#### `make up`
Menjalankan server FastAPI dengan `uvicorn`:
- macOS/Linux: `. .venv/bin/activate && uvicorn main:app --reload`
- Windows: `. .venv/Scripts/activate && uvicorn main:app --reload`

Makna argumen:
- `main:app` berarti file `main.py` dengan object `app` (FastAPI instance).
- `--reload` membuat server otomatis restart saat ada perubahan file kode.
  Ini bagus untuk development, tapi tidak untuk produksi.
Opsi `--reload` membuat server otomatis restart saat ada perubahan kode.

### Alur yang disarankan (pemula)
```bash
make build
make run
```

Setelah server jalan, buka:
```
http://127.0.0.1:8000/docs
```

Hentikan server dengan `Ctrl+C`.

---

## Ringkas: kapan pilih yang mana?
- Pilih **tanpa Makefile** jika kamu tidak punya `make` atau ingin belajar proses manualnya.
- Pilih **dengan Makefile** untuk kerja sehari-hari karena lebih cepat dan konsisten.
