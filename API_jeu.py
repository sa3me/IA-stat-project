# -*- coding: utf-8 -*-
"""
Created on Tue May 27 14:18:45 2025

@author: kusi
"""

"""
Godot (jeu) 
  → Envoie {"question": "..."}
    → Serveur Flask (ton code)
      → Appelle API OpenAI
        → Reçoit réponse IA
      → Renvoie {"answer": "..."}
  ← Godot affiche la réponse
# Ce code crée un serveur web simple avec Flask qui reçoit des questions 
# d'un jeu développé avec Godot
"""

#J'ai décidé de créer un serveur web intermédiaire qui agit comme un pont entre notre jeu 
# et l'API OpenAI. Surtout our protéger ma clé API 

from flask import Flask, request, jsonify
import openai

#configuratin clé API 
openai.api_key = "enter_the_link_to_the_key_dontwantminetobepublic"

#création appli Flask
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    question = request.json.get("question", "") #request.json récupère les données json envoyées par Godot
    
    # Appel à GPT-3.5
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", #je spécifie la version de GPT 
        messages=[
            {"role": "system", "content": "Tu es un professeur de statistiques très pédagogue. Réponds clairement et en vulgarisant à des questions sur la moyenne, l’écart-type, la variance, etc."},
            {"role": "user", "content": question}
        ]
    )
    #role system : définit le comportement de l'IA
    #role user : question posée par le joueur 

    answer = response.choices[0].message["content"] #extrait le texte de la réponse d'OpenAI
    return jsonify({"answer": answer}) #convertit la réponse (dictionnaire python) en format JSON

if __name__ == "__main__":
    app.run(port=5000)  #lancement du serveur sur le port 5000
