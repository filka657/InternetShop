import json
from flask import Flask, jsonify, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/InterShop'
db = SQLAlchemy(app)
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


@app.route('/producers/adding', methods=['POST', 'GET'])
def add_producers():
    if request.method == 'POST':
        name_producers = request.form['name']
        address_producers = request.form['address']
        telephone_producers = request.form['telephone']
        reg_producers = request.form['reg']
        requests.post('http://127.0.0.1:5000/producers/adding', json={'name_producers': name_producers,
                                                                      'address_producers': address_producers,
                                                                      'telephone_producers': telephone_producers,
                                                                      'reg_producers': reg_producers, })
        return redirect('/producers')
    else:
        return render_template("adding/add_producers.html")


@app.route('/producers/<int:id_producers>/put', methods=['POST', 'GET'])
def put_producers(id_producers):
    info_producer = requests.get(f'http://127.0.0.1:5000/producers/{id_producers}').json()
    if request.method == 'POST':
        name_producers = request.form['name']
        address_producers = request.form['address']
        telephone_producers = request.form['telephone']
        reg_producers = request.form['reg']
        requests.put(f'http://127.0.0.1:5000/producers/{id_producers}/put', json={'name_producers': name_producers,
                                                                      'address_producers': address_producers,
                                                                      'telephone_producers': telephone_producers,
                                                                      'reg_producers': reg_producers, })
        return redirect('/producers')
    else:
        return render_template("putting/put_producers.html", info_producer=info_producer)


@app.route('/producers/<int:id_producers>/delete')
def delete_producer(id_producers):
    requests.delete(f'http://127.0.0.1:5000/producers/{id_producers}/delete')
    return redirect('/producers')


@app.route('/storages')
def get_storages():
    articles = requests.get('http://127.0.0.1:5000/storages').json()
    return render_template("storages.html", menu=menu, articles=articles)


@app.route('/storages/<int:id_storages>')
def get_storage(id_storages):
    storage_info = requests.get(f'http://127.0.0.1:5000/storages/{id_storages}').json()
    articles = requests.get(f'http://127.0.0.1:5000/storage/{id_storages}').json()
    return render_template("storage.html", menu=menu, articles=articles, storage_info=storage_info)


@app.route('/stuff')
def get_stuff():
    articles = requests.get('http://127.0.0.1:5000/stuff').json()
    return render_template("stuff.html", menu=menu, articles=articles)


@app.route('/stuff/adding', methods=['POST', 'GET'])
def add_stuff():
    if request.method == 'POST':
        name_stuff = request.form['name']
        category_stuff = request.form['category']
        color_stuff = request.form['color']
        gender_stuff = request.form['gender']
        classifier_stuff = request.form['classifier']
        description_stuff = request.form['description']
        requests.post('http://127.0.0.1:5000/stuff/adding', json={'name_stuff': name_stuff,
                                                                  'category_stuff': category_stuff,
                                                                  'color_stuff': color_stuff,
                                                                  'gender_stuff': gender_stuff,
                                                                  'classifier_stuff': classifier_stuff,
                                                                  'description_stuff': description_stuff, })
        return redirect('/stuff')
    else:
        return render_template("adding/add_stuff.html")


@app.route('/stuff/<int:id_stuff>/put', methods=['POST', 'GET'])
def put_stuff(id_stuff):
    info_stuff = requests.get(f'http://127.0.0.1:5000/stuff/{id_stuff}').json()
    if request.method == 'POST':
        name_stuff = request.form['name']
        category_stuff = request.form['category']
        color_stuff = request.form['color']
        gender_stuff = request.form['gender']
        classifier_stuff = request.form['classifier']
        description_stuff = request.form['description']
        requests.put(f'http://127.0.0.1:5000/stuff/{id_stuff}/put', json={'name_stuff': name_stuff,
                                                                  'category_stuff': category_stuff,
                                                                  'color_stuff': color_stuff,
                                                                  'gender_stuff': gender_stuff,
                                                                  'classifier_stuff': classifier_stuff,
                                                                  'description_stuff': description_stuff, })
        return redirect('/stuff')
    else:
        return render_template("putting/put_stuff.html", info_stuff=info_stuff)


@app.route('/stuff/<int:id_stuff>/delete')
def delete_stuff(id_stuff):
    requests.delete(f'http://127.0.0.1:5000/stuff/{id_stuff}/delete')
    return redirect('/stuff')


@app.route('/arrivals')
def get_arrivals():
    articles = requests.get('http://127.0.0.1:5000/arrivals').json()
    return render_template("arrivals.html", menu=menu, articles=articles)


@app.route('/arrivals/adding')
def add_arrival():
    info_storages = requests.get('http://127.0.0.1:5000/storages').json()
    info_stuff = requests.get('http://127.0.0.1:5000/stuff').json()
    info_producers = requests.get('http://127.0.0.1:5000/producers').json()
    categories_of_stuff = []
    data = []
    for el in info_stuff:
        categories_of_stuff.append(el['category_stuff'])
    categories_of_stuff = list(set(categories_of_stuff))
    for j in range(len(categories_of_stuff)):
        data_stuff = []
        for i in range(len(info_stuff)):
            if info_stuff[i]['category_stuff'] == categories_of_stuff[j]:
                data_stuff.append(info_stuff[i]['name_stuff'])
        data.append({'category': categories_of_stuff[j], 'stuff': data_stuff})
    return render_template("adding/add_arrivals.html", info_storages=info_storages, info_producers=info_producers,
                           data=data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=5001)
