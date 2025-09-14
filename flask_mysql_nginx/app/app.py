from flask import Flask, render_template
import pymysql
import os

app = Flask(__name__)

query = "select @@version;"
conn = pymysql.connect(host=os.getenv("MARIADB_SERVER"),
                       port=int(os.getenv("MARIADB_PORT")),
                       user=os.getenv("MDB_USER"),
                       password=os.getenv("MDB_PASSWORD"),
                       db=os.getenv("DB_NAME"))
cursor = conn.cursor()
cursor.execute(query)
output = cursor.fetchall()

@app.route("/")
def root_path():
    return render_template("index.html")

@app.route("/mariadb")
def mariadb_version():
    return f"<h1>{output}</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)