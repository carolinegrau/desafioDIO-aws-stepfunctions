def lambda_handler(event, context):
    estoque_disponivel = 10
    pedido = event.get("pedido", {})

    if pedido.get("quantidade", 0) <= estoque_disponivel:
        return {
            "status": "Estoque disponível",
            "pedido": pedido
        }
    else:
        return {
            "status": "Estoque insuficiente",
            "pedido": pedido
        }
