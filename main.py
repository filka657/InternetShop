import json
from flask import Flask, jsonify, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/InterShop'
db = SQLAlchemy(app)


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


@app.route("/")
def start():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)