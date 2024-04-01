import psycopg2
from flask import Flask, render_template, request
import time


def connect_to_postgres():
    max_retries = 10
    retry_delay = 5  # seconds
    retries = 0

    while retries < max_retries:
        try:
            conn = psycopg2.connect(dbname='students', user='postgres', password='12345', host='postgre')
            print("Connected to PostgreSQL!")
            return conn
        except psycopg2.OperationalError as e:
            print(f"Error connecting to PostgreSQL: {e}")
            print("Retrying...")
            retries += 1
            time.sleep(retry_delay)

    print("Unable to connect to PostgreSQL after retries.")
    return None


conn = connect_to_postgres()

while conn is None:
    print("Waiting for PostgreSQL to initialize...")
    conn = connect_to_postgres()
    time.sleep(5)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        student_id = request.form["id"]
        if student_id:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM students WHERE ID = %s", (student_id,))
                student = cursor.fetchone()
                return render_template("index.html", student=student)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
