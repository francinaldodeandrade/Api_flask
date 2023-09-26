from flask import Flask, jsonify, request

app = Flask(__name__)

deliveries = [
    {
        "id": 1,
        "nome": "davi",
        "pessoa_cad": "juridica",
        "status_entrega": "em transito",
        "id_entrega": "199",
        "id_loja": "21",
        "cod_rastreio": "xyz2905BR",
        "documento": "012338333-03",
    },
    {
        "id": 2,
        "nome": "naldo",
        "pessoa_cad": "fisica",
        "status_entrega": "entregue",
        "id_entrega": "196",
        "id_loja": "19",
        "cod_rastreio": "xyz2902BR",
        "documento": "012338333-03",
    },
]


def proximo_id():
    return max(delivery["id"] for delivery in deliveries) + 1


@app.route("/entregas")
def Listar_entregas():
    return jsonify(deliveries)


@app.route("/entregas/<codigo>")
def Acompanhar_entregas(codigo):
    entrega = [delivery for delivery in deliveries["cod_rastreio"] == codigo]
    return jsonify(entrega)


@app.post("/entregas")
def add_entregas():
    if request.is_json:
        entrega = request.get_json()
        entrega["id"] = proximo_id()
        deliveries.append(entrega)
        return entrega, 201
    # return {"erro": "a requisição precisa está em formato Json"}, 415


@app.put("/entregas/<int:id_entrega>")
def atualiza_entrega(id_entrega):
    entrega = request.get_json()
    entrega_orig = [delivery for delivery in deliveries["id"] == id_entrega]

    if len(entrega_orig) == 0:
        return {"erro": "recurso não encontrado"}, 404

    entrega_orig[0] = entrega
    return entrega, 200


@app.delete("/entregas/<int:id_entrega>")
def excluir_entrega(id_entrega):
    entrega_orig = [delivery for delivery in deliveries["id"] == id_entrega]

    if len(entrega_orig) == 0:
        return {"erro": "recurso não encontrado"}, 404

    deliveries.remove(entrega_orig[0])
    return {"entrega excluida"}, 204


if __name__ == "__main__":
    app.run
