import json
from flask import Flask, jsonify, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/InterShop'
db = SQLAlchemy(app)
data = []
menu = [{'name': 'Товары', 'url': "stuff"},
        {'name': 'Склады', 'url': "storages"},
        {'name': 'Производители', 'url': "producers"},
        {'name': 'История', 'url': "arrivals"}]


@app.route("/")
def start():
    return render_template("main.html", menu=menu)


@app.route('/producers')
def get_producers():
    articles = requests.get('http://127.0.0.1:5000/producers').json()
    return render_template("producers.html", menu=menu, articles=articles)


@app.route('/storages')
def get_storages():
    articles = requests.get('http://127.0.0.1:5000/storages').json()
    return render_template("storages.html", menu=menu, articles=articles)


@app.route('/stuff')
def get_stuff():
    articles = requests.get('http://127.0.0.1:5000/stuff').json()
    return render_template("stuff.html", menu=menu, articles=articles)


@app.route('/arrivals')
def get_arrivals():
    articles = requests.get('http://127.0.0.1:5000/arrivals').json()
    return render_template("arrivals.html", menu=menu, articles=articles)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
