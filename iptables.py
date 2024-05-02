from flask import Flask
from flask import render_template
<<<<<<< HEAD
import json
=======
from dataparser import DataParser

>>>>>>> 7486b4d (maj)

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
    parser: DataParser = DataParser("static/alias.json")
    ip: list | None = parser.extract_key("ip_address")
    port: list | None = parser.extract_key("port")
    nat_rules: list = list(zip(ip, port))
    return render_template("rule_nat.html", nat_rules=nat_rules)

@app.route("/rules_nat_add")
def rules_nat_add():
    return render_template("rule_nat_add.html")


@app.route("/alias")
def alias():
    parser: DataParser = DataParser("static/alias.json")
    data: list | None = parser.extract_key("alias")
    print(data)
    return render_template("alias.html", alias=data)


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=True)
>>>>>>> 7486b4d (maj)
