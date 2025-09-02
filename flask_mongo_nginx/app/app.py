#!/usr/bin/env python3
from flask import Flask, render_template
import pymongo
import os
from dotenv import load_dotenv
import subprocess

load_dotenv()


app = Flask(__name__)
mongo_url = f"mongodb://{os.getenv("MONGO_INITDB_ROOT_USERNAME")}:{subprocess.run(["cat","/run/secrets/mongo_root_pass"],capture_output=True, text=True).stdout.strip()}@db:27017"
mongo_client = pymongo.MongoClient(mongo_url)

@app.route("/")
def main():
    try:
        mongo_client.admin.command('ping')
    except:
        return "Mongo server not found"
    return render_template("index.html")

@app.route("/mongodb")
def interaction_with_db():
    return "<h1>Site Underconstruction be patient!!!<h1>"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True)

