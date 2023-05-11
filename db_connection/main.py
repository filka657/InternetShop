import json
from flask import Flask, jsonify, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy


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

    def __repr__(self):
        return f"<Storages {self.id_storages}>"


class Producers(db.Model):
    id_producers = db.Column(db.Integer, primary_key=True)
    name_producers = db.Column(db.String(50), nullable=False)
    address_producers = db.Column(db.String(50), nullable=False)
    reg_producers = db.Column(db.String(50), nullable=False)

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


@app.route('/producers')
def get_producers():
    info = Producers.query.order_by(Producers.id_producers).all()
    data.clear()
    for el in info:
        dict_json = {'id_producers': el.id_producers, 'name_producers': el.name_producers,
                     'address_producers': el.address_producers, 'reg_producers': el.reg_producers}
        data.append(dict_json)
    articles = jsonify(data)
    return articles


@app.route('/storages')
def get_storages():
    info = Storages.query.order_by(Storages.id_storages).all()
    data.clear()
    for el in info:
        dict_json = {'id_storages': el.id_storages, 'name_storages': el.name_storages,
                     'address_storages': el.address_storages,}
        data.append(dict_json)
    articles = jsonify(data)
    return articles


@app.route('/stuff')
def get_stuff():
    info = Stuff.query.order_by(Stuff.id_stuff).all()
    data.clear()
    for el in info:
        dict_json = {'id_stuff': el.id_stuff, 'name_stuff': el.name_stuff, 'category_stuff': el.category_stuff,
                     'color_stuff': el.reg_producers, 'gender_stuff': el.gender_stuff,
                     'classifier_stuff': el.classifier_stuff, 'description_stuff': el.description_stuff,
                     }
        data.append(dict_json)
    articles = jsonify(data)
    return articles


@app.route('/arrivals')
def get_arrivals():
    info = Arrivals.query.order_by(Arrivals.id_arrivals).all()
    data.clear()
    for el in info:
        dict_json = {'id_arrivals': el.id_arrivals, 'stuffid_arrivals': el.name_stuff, 'category_stuff': el.category_stuff,
                     'color_stuff': el.reg_producers, 'gender_stuff': el.gender_stuff,
                     'classifier_stuff': el.classifier_stuff, 'description_stuff': el.description_stuff,
                     }
        data.append(dict_json)
    articles = jsonify(data)
    return articles


if __name__ == '__main__':
    app.run(debug=True)
