def lambda_handler(event, context):
    pedido = {
        "id": event.get("pedidoId", "12345"),
        "produto": event.get("produto", "Camisa"),
        "quantidade": event.get("quantidade", 1)
    }

    return {
        "status": "Pedido recebido",
        "pedido": pedido
    }
