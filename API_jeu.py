# -*- coding: utf-8 -*-
"""
Created on Tue May 27 14:18:45 2025

@author: kusi
"""

from flask import Flask, request, jsonify
import openai


openai.api_key = "enter_the_link_to_the_key_dontwantminetobepublic"

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    question = request.json.get("question", "")
    
    # Appel à GPT-3.5
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Tu es un professeur de statistiques très pédagogue. Réponds clairement à des questions sur la moyenne, l’écart-type, la variance, etc."},
            {"role": "user", "content": question}
        ]
    )
    
    answer = response.choices[0].message["content"]
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(port=5000)