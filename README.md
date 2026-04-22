Panduan untuk Menjalankan Aplikasi


1. Clone: git clone https://github.com/J0MSNGRpL2k24/simple-todoList-with-django.git

2. Buat Virtual Env: python -m venv .venv (atau uv venv jika menggunakan uv).

3. Aktifkan Env: .venv\Scripts\activate (Windows) atau source .venv/bin/activate (Mac/Linux).

4. Install Library: pip install -r requirements.txt (atau uv sync).

5. Migrate Database: python manage.py migrate (ini akan membuat file db.sqlite3 baru di laptop anda).

Run Server: python manage.py runserver.
