from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hacked_TV | Bot online!\n------------------------\nBot feito por Hacked_TV\n------------------------"

def run():
  app.run(host='0.0.0.0',port=8080)

def Reping():
    t = Thread(target=run)
    t.start()