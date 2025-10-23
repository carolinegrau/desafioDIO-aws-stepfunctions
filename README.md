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

Durante a execução do fluxo, a etapa `EnviarConfirmacao` falhou com o seguinte erro:

```json
"errorMessage": "Erro: Falha ao enviar e-mail: Error: connect ECONNREFUSED ::1:587"

## 🔧 Diagnóstico:
A função tentava enviar e-mail via SMTP local, o que não é permitido no ambiente da AWS Lambda.

## ✅ Solução aplicada:
Removemos a tentativa de conexão SMTP

Simulamos o envio com uma mensagem de confirmação

Garantimos que o fluxo pudesse ser executado com sucesso

## 📘 Aprendizados
Como criar e conectar funções Lambda em Python

Como montar um fluxo com AWS Step Functions usando JSON

Como lidar com erros de integração e aplicar correções

Como documentar um projeto técnico de forma clara e objetiva

## 🔗 Referências
Documentação AWS Step Functions

Documentação AWS Lambda

Desafio DIO - Orquestração com Step Functions

## ✅ Status do projeto
✔️ Fluxo funcional ✔️ Correção aplicada ✔️ Documentação concluída ✔️ Pronto para entrega na DIO 🚀


