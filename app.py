# -*- coding: utf-8 -*-
import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

python = {"top_p": 0.9, "frequency_penalty":0.5, "presence_penalty":0.5, "temperature":0.7, "max_tokens":3000, "model":"text-davinci-003"}
java = {"top_p": 1.0, "frequency_penalty":0.2, "presence_penalty":0.2, "temperature":0.7, "max_tokens":3000, "model":"text-davinci-003"}
text = {"top_p": 1.0, "frequency_penalty":0.0, "presence_penalty":0.0, "temperature":0.5, "max_tokens":2000, "model":"text-davinci-003"}
js = {"top_p": 1.0, "frequency_penalty":0.0, "presence_penalty":0.0, "temperature":0.7, "max_tokens":3000, "model":"text-davinci-003"}
img = {"top_p": 1.0, "frequency_penalty":0.0, "presence_penalty":0.0, "temperature":0.7, "max_tokens":50, "model":"openai-gpt"}
model = {"python":python, "java":java, "text":text, "js":js, "img":img}

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":

        q = str(request.form["query"])
        m = str(request.form["model"])
        link = "link"
        result = "img"
        
        if m == "img":
            response = openai.Image.create(
            prompt=q,
            n=1,
            size="512x512"
            )
            link = str(response['data'][0]['url'])       
            print("URL =======\n"+link)
            return render_template("index.html", query=q, link=link)

        else:
            print(m + " =======")
            response = openai.Completion.create(
            model=model[m]["model"],
            prompt=q,
            temperature=model[m]["temperature"],
            max_tokens=model[m]["max_tokens"],
            top_p=model[m]["top_p"],
            frequency_penalty=model[m]["frequency_penalty"],
            presence_penalty=model[m]["presence_penalty"]
            )
            result = str(response.choices[0].text)
            return redirect(url_for("index", query=q, result=result))

    result = request.args.get("result")
    q = request.args.get("query")
    return render_template("index.html", query=q, result=result)
