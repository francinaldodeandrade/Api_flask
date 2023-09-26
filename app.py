from flask import Flask, jsonify

app = Flask(__name__)

deliveries = [
    {
        "id": 1,
        "nome": "davi",
        "pessoa_cad": "juridica",
        "status_entrega": "em transito",
        "id_pedido": 199,
        "id_loja": 21,
        "cod_rasteio": "xyz2905BR",
    },
    {
        "id": 2,
        "nome": "naldo",
        "pessoa_cad": "fisica",
        "status_entrega": "entregue",
        "id_pedido": 196,
        "id_loja": 19,
        "cod_rasteio": "xyz2902BR",
    },
]


@app.route("/entregas")
def Listar_entregas():
    return jsonify(deliveries)


if __name__ == "__main__":
    app.run
