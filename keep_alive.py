"""keep_alive.py — Health check server para Render + CronJob"""
from flask import Flask
from threading import Thread
import os
import logging

# Silenciar logs de werkzeug para no ensuciar la consola del bot
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Almacén Bot — Online", 200

@app.route('/health')
def health():
    return "OK", 200

@app.route('/ping')
def ping():
    return "pong", 200

def run():
    port = int(os.getenv("PORT", 8080))
    # use_reloader=False y threaded=True son críticos
    app.run(host='0.0.0.0', port=port, use_reloader=False, threaded=True)

def keep_alive():
    t = Thread(target=run, daemon=True)
    t.start()
    print("✅ Keep-alive server iniciado", flush=True)
