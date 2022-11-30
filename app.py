import numpy as np
from flask import Flask, request, render_template, jsonify
import pickle

# Create flask app
app = Flask(__name__)

# Load the model pickle
model_paracetamol = pickle.load(open("modelParacetamol.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")