def lambda_handler(event, context):
    pedido = event.get("pedido", {})
    mensagem = f"Pedido {pedido.get('id')} confirmado com sucesso!"

    print(f"[SIMULADO] Enviando e-mail: {mensagem}")

    return {
        "status": "Confirmação simulada",
        "mensagem": mensagem,
        "pedido": pedido
    }
