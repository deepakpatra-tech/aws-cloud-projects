from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = "cloudx.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS service_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            service TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Open',
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def home():
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT * FROM service_requests ORDER BY id DESC"
    ).fetchall()
    conn.close()
    return render_template("index.html", requests=rows)


@app.route("/add", methods=["POST"])
def add_request():
    customer_name = request.form["customer_name"].strip()
    service = request.form["service"].strip()

    if customer_name and service:
        conn = get_db_connection()
        conn.execute(
            """
            INSERT INTO service_requests (customer_name, service, status, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (
                customer_name,
                service,
                "Open",
                datetime.now().strftime("%Y-%m-%d %H:%M")
            )
        )
        conn.commit()
        conn.close()

    return redirect(url_for("home"))


@app.route("/update/<int:request_id>", methods=["POST"])
def update_request(request_id):
    status = request.form["status"]

    conn = get_db_connection()
    conn.execute(
        "UPDATE service_requests SET status = ? WHERE id = ?",
        (status, request_id)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("home"))


@app.route("/delete/<int:request_id>", methods=["POST"])
def delete_request(request_id):
    conn = get_db_connection()
    conn.execute(
        "DELETE FROM service_requests WHERE id = ?",
        (request_id,)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("home"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
