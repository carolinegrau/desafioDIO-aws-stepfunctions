def lambda_handler(event, context):
    pedido = event.get("pedido", {})
    pagamento_aprovado = True

    if pagamento_aprovado:
        return {
            "status": "Pagamento aprovado",
            "pedido": pedido
        }
    else:
        return {
            "status": "Pagamento recusado",
            "pedido": pedido
        }
