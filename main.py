from flask import Flask
from flask import jsonify
from flask import render_template

from model import Stock


app = Flask(__name__)

import migration

migration.run()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/stock/<symbol>")
def by_symbol(symbol):
    return jsonify(trend=[stock.serialize() for stock in Stock.objects(Stock.name == symbol).allow_filtering()])


if __name__ == "__main__":
    app.run(debug=True)
