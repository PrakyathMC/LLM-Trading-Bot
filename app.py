from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os



app = Flask(__name__)

load_dotenv()

@app.route("/")
def index():
    return render_template("chat.html")

if __name__ == '__main__':
    app.run(debug=True) 