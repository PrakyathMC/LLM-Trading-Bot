from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
from tradingbot.retrieval_generation import generation
from tradingbot.data_ingestion import ingestdata

app = Flask(__name__)
#loading .env
load_dotenv()

vstore=ingestdata("done")
chain=generation(vstore)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    result=chain.invoke(input)
    print("Response : ", result)
    return str(result)

if __name__ == '__main__':
    app.run(debug= True)