# -*- coding: utf-8 -*-
import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

python = {"top_p": 0.9, "frequency_penalty":0.5, "presence_penalty":0.5, "temperature":0.7, "max_tokens":3000}
java = {"top_p": 1.0, "frequency_penalty":0.2, "presence_penalty":0.2, "temperature":0.7, "max_tokens":3000}
text = {"top_p": 1.0, "frequency_penalty":0.0, "presence_penalty":0.0, "temperature":0.5, "max_tokens":2000}
js = {"top_p": 1.0, "frequency_penalty":0.0, "presence_penalty":0.0, "temperature":0.7, "max_tokens":3000}
img = {"top_p": 1.0, "frequency_penalty":0.0, "presence_penalty":0.0, "temperature":0.7, "max_tokens":3000, "model":"image-davinci-003"}
model = {"python":python, "java":java, "text":text, "js":js}

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":

        q = request.form["query"]
        m = request.form["model"]

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=q,
            temperature=model[m]["temperature"],
            max_tokens=model[m]["max_tokens"],
            top_p=model[m]["top_p"],
            frequency_penalty=model[m]["frequency_penalty"],
            presence_penalty=model[m]["presence_penalty"]
        )
        return redirect(url_for("index", query=q, result=str(response.choices[0].text)))

    result = request.args.get("result")
    query = request.args.get("query")
    return render_template("index.html", query=query, result=result)
