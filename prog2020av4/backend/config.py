from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

caminho = os.path.dirname(os.path.abspath(__file__))
caminho_bd = os.path.join(caminho, 'bancodedados.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{caminho_bd}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
bd = SQLAlchemy(app)
