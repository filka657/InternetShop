import json
from flask import Flask, jsonify, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/InterShop'
db = SQLAlchemy(app)


@app.route("/")
def start():
    return render_template("main.html")


@app.route('/producers')
def get_producers():
    articles = requests.get('http://127.0.0.1:5000/producers').json()
    return render_template("producers.html", articles=articles)


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
    return render_template("storages.html", articles=articles)


@app.route('/storages/<int:id_storages>')
def get_storage(id_storages):
    storage_info = requests.get(f'http://127.0.0.1:5000/storages/{id_storages}').json()
    articles = requests.get(f'http://127.0.0.1:5000/storage/{id_storages}').json()
    return render_template("storage.html", articles=articles, storage_info=storage_info)


@app.route('/stuff')
def get_stuff():
    articles = requests.get('http://127.0.0.1:5000/stuff').json()
    return render_template("stuff.html", articles=articles)


@app.route('/stuff/<int:id_stuff>')
def balance_stuff(id_stuff):
    articles = []
    dict_json1 = []
    dict_json2 = []
    dict_json3 = []
    info_storages = requests.get('http://127.0.0.1:5000/storages').json()
    info_storage1 = requests.get('http://127.0.0.1:5000/storage/1').json()
    info_storage2 = requests.get('http://127.0.0.1:5000/storage/2').json()
    info_storage3 = requests.get('http://127.0.0.1:5000/storage/3').json()
    for el1 in info_storage1:
        if el1['stuffid_storage'] != id_stuff:
            dict_json1 = {'name_storages': info_storages[0]['name_storages'], 'address_storages': info_storages[0]['address_storages'],
                          'telephone_storages': info_storages[0]['telephone_storages'], 'balance_stuff': 0, }
        else:
            dict_json1 = {'name_storages': info_storages[0]['name_storages'], 'address_storages': info_storages[0]['address_storages'],
                          'telephone_storages': info_storages[0]['telephone_storages'], 'balance_stuff': el1['quentitystuff_storage'], }
            break
    for el2 in info_storage2:
        if el2['stuffid_storage'] != id_stuff:
            dict_json2 = {'name_storages': info_storages[1]['name_storages'], 'address_storages': info_storages[1]['address_storages'],
                          'telephone_storages': info_storages[1]['telephone_storages'], 'balance_stuff': 0, }
        else:
            dict_json2 = {'name_storages': info_storages[1]['name_storages'], 'address_storages': info_storages[1]['address_storages'],
                          'telephone_storages': info_storages[1]['telephone_storages'], 'balance_stuff': el2['quentitystuff_storage'], }
            break
    for el3 in info_storage3:
        if el3['stuffid_storage'] != id_stuff:
            dict_json3 = {'name_storages': info_storages[2]['name_storages'], 'address_storages': info_storages[2]['address_storages'],
                          'telephone_storages': info_storages[2]['telephone_storages'], 'balance_stuff': 0, }
        else:
            dict_json3 = {'name_storages': info_storages[2]['name_storages'], 'address_storages': info_storages[2]['address_storages'],
                          'telephone_storages': info_storages[2]['telephone_storages'], 'balance_stuff': el3['quentitystuff_storage'], }
            break
    articles.append(dict_json1)
    articles.append(dict_json2)
    articles.append(dict_json3)
    return render_template("balance_stuff.html", articles=articles)


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
    return render_template("arrivals.html", articles=articles)


@app.route('/arrivals/adding', methods=['POST', 'GET'])
def add_arrival():
    info_storages = requests.get('http://127.0.0.1:5000/storages').json()
    info_stuff = requests.get('http://127.0.0.1:5000/stuff').json()
    info_producers = requests.get('http://127.0.0.1:5000/producers').json()
    data = get_categories(info_stuff)
    if request.method == 'POST':
        stuffid_arrivals = request.form['stuff']
        quentity_arrivals = request.form['quentity']
        prodid_arrivals = request.form['producers']
        storeid_arrivals = request.form['storage']
        invoice_arrivals = request.form['invoice']
        check_arrivals = request.form['check']

        requests.post('http://127.0.0.1:5000/arrivals/adding', json={'stuffid_arrivals': stuffid_arrivals,
                                                                     'quentity_arrivals': quentity_arrivals,
                                                                     'prodid_arrivals': prodid_arrivals,
                                                                     'storeid_arrivals': storeid_arrivals,
                                                                     'invoice_arrivals': invoice_arrivals,
                                                                     'check_arrivals': check_arrivals})
        return redirect('/arrivals')
    else:
        return render_template("adding/add_arrivals.html", info_storages=info_storages, info_producers=info_producers,
                           data=data)


@app.route('/arrivals/<int:id_arrivals>/delete')
def delete_arrivals(id_arrivals):
    requests.delete(f'http://127.0.0.1:5000/arrivals/{id_arrivals}/delete')
    return redirect('/arrivals')


def get_categories(info_stuff):
    categories_of_stuff = []
    data = []
    for el in info_stuff:
        categories_of_stuff.append(el['category_stuff'])
    categories_of_stuff = sorted(list(set(categories_of_stuff)))
    for j in range(len(categories_of_stuff)):
        data_stuff = []
        for i in range(len(info_stuff)):
            if info_stuff[i]['category_stuff'] == categories_of_stuff[j]:
                data_stuff.append({'key': info_stuff[i]['id_stuff'], 'value': info_stuff[i]['name_stuff']})
        data.append({'category': categories_of_stuff[j], 'stuff': data_stuff})
    return data


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=5001)
