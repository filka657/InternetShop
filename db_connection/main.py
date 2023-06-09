import json
from flask import Flask, jsonify, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/InterShop'
db = SQLAlchemy(app)
data = []


class Stuff(db.Model):
    id_stuff = db.Column(db.Integer, primary_key=True)
    name_stuff = db.Column(db.String(30), nullable=False)
    category_stuff = db.Column(db.String(30), nullable=False)
    color_stuff = db.Column(db.String(30))
    gender_stuff = db.Column(db.String(30))
    classifier_stuff = db.Column(db.Integer, nullable=False)
    description_stuff = db.Column(db.String(100))

    def __repr__(self):
        return f"<Stuff {self.id_stuff}>"


class Storages(db.Model):
    id_storages = db.Column(db.Integer, primary_key=True)
    name_storages = db.Column(db.String(50), nullable=False)
    address_storages = db.Column(db.String(50), nullable=False)
    telephone_storages = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Storages {self.id_storages}>"


class Producers(db.Model):
    id_producers = db.Column(db.Integer, primary_key=True)
    name_producers = db.Column(db.String(50), nullable=False)
    address_producers = db.Column(db.String(50), nullable=False)
    reg_producers = db.Column(db.String(50), nullable=False)
    telephone_producers = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Producers {self.id_producers}>"


class Arrivals(db.Model):
    id_arrivals = db.Column(db.Integer, primary_key=True)
    stuffid_arrivals = db.Column(db.Integer, db.ForeignKey('stuff.id_stuff'))
    quentity_arrivals = db.Column(db.Integer, nullable=False)
    prodid_arrivals = db.Column(db.Integer, db.ForeignKey('producers.id_producers'))
    storeid_arrivals = db.Column(db.Integer, db.ForeignKey('storages.id_storages'))
    datetime_arrivals = db.Column(db.String(50), nullable=False)
    invoice_arrivals = db.Column(db.String(50), nullable=False)
    check_arrivals = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Arrivals {self.id_arrivals}>"


class Storage1(db.Model):
    stuffid_storage = db.Column(db.Integer, db.ForeignKey('stuff.id_stuff'), primary_key=True)
    prodid_storage = db.Column(db.Integer, db.ForeignKey('producers.id_producers'))
    quentitystuff_storage = db.Column(db.Integer)

    def __repr__(self):
        return f"<Storage1 {self.stuffid_storage1}>"


class Storage2(db.Model):
    stuffid_storage = db.Column(db.Integer, db.ForeignKey('stuff.id_stuff'), primary_key=True)
    prodid_storage = db.Column(db.Integer, db.ForeignKey('producers.id_producers'))
    quentitystuff_storage = db.Column(db.Integer)

    def __repr__(self):
        return f"<Storage2 {self.stuffid_storage2}>"


class Storage3(db.Model):
    stuffid_storage = db.Column(db.Integer, db.ForeignKey('stuff.id_stuff'), primary_key=True)
    prodid_storage = db.Column(db.Integer, db.ForeignKey('producers.id_producers'))
    quentitystuff_storage = db.Column(db.Integer)

    def __repr__(self):
        return f"<Storage3 {self.stuffid_storage3}>"


@app.route('/producers')
def get_producers():
    info = Producers.query.order_by(Producers.id_producers).all()
    data.clear()
    for el in info:
        dict_json = {'id_producers': el.id_producers, 'name_producers': el.name_producers,
                     'address_producers': el.address_producers, 'telephone_producers': el.telephone_producers,
                     'reg_producers': el.reg_producers, }
        data.append(dict_json)
    articles = jsonify(data)
    return articles


@app.route('/producers/adding', methods=['POST'])
def add_producer():
    with app.app_context():
        name_producers = request.json['name_producers']
        address_producers = request.json['address_producers']
        reg_producers = request.json['reg_producers']
        telephone_producers = request.json['telephone_producers']
        producer = Producers(name_producers=name_producers, address_producers=address_producers,
                             reg_producers=reg_producers, telephone_producers=telephone_producers)
        db.session.add(producer)
        db.session.commit()


@app.route('/producers/<int:id_producers>', )
def get_one_producer(id_producers):
    info_producer = Producers.query.get_or_404(id_producers)
    dict_json = {'id_producers': info_producer.id_producers, 'name_producers': info_producer.name_producers,
                 'address_producers': info_producer.address_producers, 'telephone_producers': info_producer.telephone_producers,
                 'reg_producers': info_producer.reg_producers, }
    articles = jsonify(dict_json)
    return articles


@app.route('/producers/<int:id_producers>/put', methods=['PUT'])
def put_producer(id_producers):
    info_producer = Producers.query.get_or_404(id_producers)
    info_producer.name_producers = request.json['name_producers']
    info_producer.address_producers = request.json['address_producers']
    info_producer.telephone_producers = request.json['telephone_producers']
    info_producer.reg_producers = request.json['reg_producers']

    db.session.commit()


@app.route('/producers/<int:id_producers>/delete')
def delete_producer(id_producers):
    info_producer = Producers.query.get_or_404(id_producers)
    db.session.delete(info_producer)
    db.session.commit()
    return redirect('http://127.0.0.1:5001/producers')


@app.route('/storages')
def get_storages():
    info = Storages.query.order_by(Storages.id_storages).all()
    data.clear()
    for el in info:
        dict_json = {'id_storages': el.id_storages, 'name_storages': el.name_storages,
                     'address_storages': el.address_storages, 'telephone_storages': el.telephone_storages, }
        data.append(dict_json)
    articles = jsonify(data)
    return articles


@app.route('/storages/<int:id_storage>')
def get_one_storage(id_storage):
    info_storage = Storages.query.get_or_404(id_storage)
    data.clear()
    dict_json = {'id_storages': info_storage.id_storages, 'name_storages': info_storage.name_storages,
        'address_storages': info_storage.address_storages, 'telephone_storages': info_storage.telephone_storages}
    data.append(dict_json)
    articles = jsonify(data)
    return articles


@app.route('/stuff')
def get_stuff():
    info = Stuff.query.order_by(Stuff.id_stuff).all()
    data.clear()
    for el in info:
        dict_json = {'id_stuff': el.id_stuff, 'name_stuff': el.name_stuff, 'category_stuff': el.category_stuff,
                     'color_stuff': el.color_stuff, 'gender_stuff': el.gender_stuff,
                     'classifier_stuff': el.classifier_stuff, 'description_stuff': el.description_stuff,
                     }
        data.append(dict_json)
    articles = jsonify(data)
    return articles


@app.route('/stuff/<int:id_stuff>')
def get_one_stuff(id_stuff):
    info_stuff = Stuff.query.get_or_404(id_stuff)
    dict_json = {'id_stuff': info_stuff.id_stuff, 'name_stuff': info_stuff.name_stuff, 'category_stuff': info_stuff.category_stuff,
                 'color_stuff': info_stuff.color_stuff, 'gender_stuff': info_stuff.gender_stuff,
                 'classifier_stuff': info_stuff.classifier_stuff, 'description_stuff': info_stuff.description_stuff,
                 }
    articles = jsonify(dict_json)
    return articles


@app.route('/stuff/adding', methods=['POST'])
def add_stuff():
    with app.app_context():
        name_stuff = request.json['name_stuff']
        category_stuff = request.json['category_stuff']
        color_stuff = request.json['color_stuff']
        gender_stuff = request.json['gender_stuff']
        classifier_stuff = request.json['classifier_stuff']
        description_stuff = request.json['description_stuff']
        stuff = Stuff(name_stuff=name_stuff, category_stuff=category_stuff,
                      color_stuff=color_stuff, gender_stuff=gender_stuff,
                      classifier_stuff=classifier_stuff, description_stuff=description_stuff)
        db.session.add(stuff)
        db.session.commit()


@app.route('/stuff/<int:id_stuff>/put', methods=['PUT'])
def put_stuff(id_stuff):
    info_stuff = Stuff.query.get_or_404(id_stuff)
    info_stuff.name_stuff = request.json['name_stuff']
    info_stuff.category_stuff = request.json['category_stuff']
    info_stuff.color_stuff = request.json['color_stuff']
    info_stuff.gender_stuff = request.json['gender_stuff']
    info_stuff.classifier_stuff = request.json['classifier_stuff']
    info_stuff.description_stuff = request.json['description_stuff']

    db.session.commit()


@app.route('/stuff/<int:id_stuff>/delete')
def delete_stuff(id_stuff):
    info_stuff = Stuff.query.get_or_404(id_stuff)
    db.session.delete(info_stuff)
    db.session.commit()
    return redirect('http://127.0.0.1:5001/stuff')


@app.route('/arrivals')
def get_arrivals():
    info = Arrivals.query.order_by(Arrivals.id_arrivals.desc()).all()
    data.clear()
    for el in info:
        dict_json = {'id_arrivals': el.id_arrivals, 'stuffid_arrivals': el.stuffid_arrivals, 'quentity_arrivals': el.quentity_arrivals,
                     'prodid_arrivals': el.prodid_arrivals, 'storeid_arrivals': el.storeid_arrivals,
                     'datetime_arrivals': el.datetime_arrivals, 'invoice_arrivals': el.invoice_arrivals,
                     'check_arrivals': el.check_arrivals,}
        data.append(dict_json)
    articles = jsonify(data)
    return articles


@app.route('/arrivals/adding', methods=['POST'])
def add_arrivals():
    with app.app_context():
        stuffid_arrivals = request.json['stuffid_arrivals']
        quentity_arrivals = request.json['quentity_arrivals']
        prodid_arrivals = request.json['prodid_arrivals']
        storeid_arrivals = request.json['storeid_arrivals']
        datetime_arrivals = datetime.now(pytz.timezone('Europe/Moscow')).strftime("%Y-%m-%d %H:%M:%S")
        invoice_arrivals = request.json['invoice_arrivals']
        check_arrivals = request.json['check_arrivals']
        arrival = Arrivals(stuffid_arrivals=stuffid_arrivals, quentity_arrivals=quentity_arrivals,
                      prodid_arrivals=prodid_arrivals, storeid_arrivals=storeid_arrivals,
                      datetime_arrivals=datetime_arrivals,
                      invoice_arrivals=invoice_arrivals, check_arrivals=check_arrivals)
        db.session.add(arrival)
        if storeid_arrivals == '1':
            if Storage1.query.get(stuffid_arrivals):
                storage = Storage1.query.get(stuffid_arrivals)
                storage.quentitystuff_storage = str(int(storage.quentitystuff_storage) + int(quentity_arrivals))
            else:
                storage = Storage1(stuffid_storage=stuffid_arrivals, prodid_storage=prodid_arrivals,
                               quentitystuff_storage=quentity_arrivals)
        elif storeid_arrivals == '2':
            if Storage2.query.get(stuffid_arrivals):
                storage = Storage2.query.get(stuffid_arrivals)
                storage.quentitystuff_storage = str(int(storage.quentitystuff_storage) + int(quentity_arrivals))
            else:
                storage = Storage2(stuffid_storage=stuffid_arrivals, prodid_storage=prodid_arrivals,
                               quentitystuff_storage=quentity_arrivals)
        elif storeid_arrivals == '3':
            if Storage3.query.get(stuffid_arrivals):
                storage = Storage3.query.get(stuffid_arrivals)
                storage.quentitystuff_storage = str(int(storage.quentitystuff_storage) + int(quentity_arrivals))
            else:
                storage = Storage3(stuffid_storage=stuffid_arrivals, prodid_storage=prodid_arrivals,
                               quentitystuff_storage=quentity_arrivals)
        db.session.add(storage)
        db.session.commit()


@app.route('/arrivals/<int:id_arrivals>/delete')
def delete_arrivals(id_arrivals):
    info_arrivals = Arrivals.query.get_or_404(id_arrivals)
    db.session.delete(info_arrivals)
    db.session.commit()
    return redirect('http://127.0.0.1:5001/arrivals')


@app.route('/storage/1')
def get_storage1():
    info = Storage1.query.order_by(Storage1.stuffid_storage).all()
    data.clear()
    for el in info:
        dict_json = {'stuffid_storage': el.stuffid_storage, 'prodid_storage': el.prodid_storage,
                     'quentitystuff_storage': el.quentitystuff_storage,}
        data.append(dict_json)
    articles = jsonify(data)
    return articles


@app.route('/storage/2')
def get_storage2():
    info = Storage2.query.order_by(Storage2.stuffid_storage).all()
    data.clear()
    for el in info:
        dict_json = {'stuffid_storage': el.stuffid_storage, 'prodid_storage': el.prodid_storage,
                     'quentitystuff_storage': el.quentitystuff_storage,}
        data.append(dict_json)
    articles = jsonify(data)
    return articles


@app.route('/storage/3')
def get_storage3():
    info = Storage3.query.order_by(Storage3.stuffid_storage).all()
    data.clear()
    for el in info:
        dict_json = {'stuffid_storage': el.stuffid_storage, 'prodid_storage': el.prodid_storage,
                     'quentitystuff_storage': el.quentitystuff_storage,}
        data.append(dict_json)
    articles = jsonify(data)
    return articles


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
