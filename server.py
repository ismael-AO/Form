from flask import Flask, request, render_template, make_response, jsonify
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = json.loads(request.data.decode("utf-8"))

    value1 = int(data["value1"])
    value2 = int(data["value2"])
    math_sign = data["math_sign"]

    resul = 0

    if math_sign == "+":
        resul = value1 + value2

    if math_sign == "-":
        resul = value1 - value2

    if math_sign == "*":
        resul = value1 * value2

    if math_sign == "/":
        resul = value1 / value2

    return make_response(jsonify({"result": resul}))


if __name__ == "__main__":
    app.run(debug=True)
