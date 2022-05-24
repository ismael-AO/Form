from flask import Flask, request, render_template, make_response, jsonify
import json
from calculate import Calcular


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = json.loads(request.data.decode("utf-8"))

    calcular = Calcular()
    try:
        value1 = float(data["value1"])
        expoente = int(data["value2"])
        math_sign = data["math_sign"]

        result = 0

        if math_sign == "expoente":
            result = calcular.expoente(expoente, value1)

        if math_sign == "raiz_quadrada":
            result = calcular.raiz_quadrada(value1)

        if math_sign == "logaritmo":
            result = calcular.logaritmo(value1)

        return make_response(jsonify({"result": result}))
    except:
        return make_response(jsonify({"result": "Erro ao calcular"}))


if __name__ == "__main__":
    app.run(debug=True)
