# 🛒 Fluxo de Processamento de Pedido com AWS Step Functions

Este projeto foi desenvolvido como parte do desafio da DIO para consolidar conhecimentos sobre **AWS Step Functions** e **Lambda Functions**. O objetivo foi criar um fluxo automatizado de processamento de pedidos, simulando um sistema de e-commerce.

---

## 🚀 Objetivo

Construir um workflow completo com AWS Step Functions que orquestra funções Lambda para:

1. Receber um pedido
2. Verificar disponibilidade de estoque
3. Processar pagamento
4. Enviar confirmação ao cliente

---

## 🧰 Tecnologias utilizadas

- AWS Lambda (Python)
- AWS Step Functions
- IAM (controle de permissões)
- GitHub (documentação e entrega)

---


---

## 🧠 Lógica do fluxo

Cada etapa do fluxo foi implementada como uma função Lambda em Python:

### 1️⃣ `receber_pedido.py`
Recebe os dados do pedido e retorna um objeto com ID, produto e quantidade.

### 2️⃣ `verificar_estoque.py`
Simula a verificação de estoque. Se a quantidade for menor ou igual a 10, retorna "Estoque disponível".

### 3️⃣ `processar_pagamento.py`
Simula o pagamento com uma resposta positiva fixa ("Pagamento aprovado").

### 4️⃣ `enviar_confirmacao.py`
Inicialmente tentava enviar e-mail via SMTP, mas gerava erro de conexão (`ECONNREFUSED ::1:587`).  
**Correção aplicada:** substituímos o envio real por uma **simulação**, retornando uma mensagem de sucesso e registrando o envio com `print()`.

---
## 🐞 Erro encontrado e solução

Durante a execução da função, a etapa `EnviarConfirmacao` falhou com o seguinte erro:
(`ECONNREFUSED ::1:587`)


### 🔍 Diagnóstico
O erro está relacionado ao envio de e-mail via SMTP local. O endereço `::1` representa o localhost, e a porta 587 é usada para envio de e-mails. Como o ambiente da AWS Lambda não possui um servidor SMTP local, a conexão foi recusada.

### ✅ Solução aplicada
- Removemos a tentativa de envio real via SMTP
- Substituímos por uma **simulação de envio**, retornando uma mensagem de sucesso
- A função passou a executar corretamente dentro do fluxo

### 📘 Aprendizados
- Como criar e testar funções Lambda em Python
- Como lidar com erros de conexão SMTP em ambientes serverless
- Como simular funcionalidades para manter o fluxo funcional

### 🧾 Conclusão
Documentar um projeto técnico de forma clara e objetiva é essencial para aprendizado contínuo e futuras implementações. Esta experiência reforçou a importância de entender os limites do ambiente e aplicar soluções criativas para manter a integridade do sistema.

