from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


# =========================
# DATABASE
# =========================

def init_db():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pesanan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            jasa TEXT NOT NULL,
            deskripsi TEXT NOT NULL,
            status TEXT DEFAULT 'Menunggu'
        )
    """)

    conn.commit()
    conn.close()


# =========================
# HALAMAN HOME
# =========================

@app.route("/")
def home():

    return render_template("index.html")


# =========================
# SIMPAN PESANAN
# =========================

@app.route("/pesan", methods=["POST"])
def pesan():

    nama = request.form["nama"]
    jasa = request.form["jasa"]
    deskripsi = request.form["deskripsi"]

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pesanan
        (nama, jasa, deskripsi)
        VALUES (?, ?, ?)
    """, (nama, jasa, deskripsi))

    conn.commit()
    conn.close()

    return redirect("/admin")


# =========================
# ADMIN
# =========================

@app.route("/admin")
def admin():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pesanan")

    pesanan = cursor.fetchall()

    conn.close()

    return render_template(
        "admin.html",
        pesanan=pesanan
    )


# =========================
# RUN
# =========================

if __name__ == "__main__":

    init_db()

    app.run(debug=True)