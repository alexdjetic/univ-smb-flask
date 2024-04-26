from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("start.html")


@app.route("/start")
def start():
    return render_template("start.html")


@app.route("/rules_filter")
def rules_filter():
    return render_template("rule_filter.html")


@app.route("/rules_nat")
def rules_nat():
    return render_template("rule_nat.html")


@app.route("/rules_nat_add")
def rules_nat_add():
    return render_template("rule_nat_add.html")


@app.route("/alias")
def alias():
    return render_template("alias.html")


if __name__ == "__main__":
    app.run(debug=False)