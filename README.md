# 🔹 Construindo um Sistema Bancário em Python 🏦💰

## 📌 Descrição
Você foi contratado para desenvolver um sistema bancário simples utilizando Python! O sistema deve permitir que o usuário realize depósitos, saques, visualize o extrato e encerre o programa. Todas as operações devem ser registradas e exibidas corretamente.

## 📌 Objetivo:
Criar um sistema funcional que simule operações bancárias básicas.

## 📌 Regras do Sistema
- 1️⃣ Depósito

O usuário pode inserir um valor positivo e adicioná-lo ao saldo da conta.
A operação deve ser registrada no extrato.

- 2️⃣ Saque

O usuário pode retirar um valor do saldo da conta.
A operação deve ser registrada no extrato.

- 3️⃣ Extrato

Exibe todas as transações feitas (depósitos e saques).
Exibe o saldo atual da conta.

- 4️⃣ Sair

O sistema deve permitir que o usuário encerre o programa digitando a opção correspondente.

- 5️⃣ Validações (Bônus)

O sistema não pode permitir saques se o saldo for insuficiente.
O usuário não pode depositar valores negativos.

## 📌 Entrada
O usuário interage com um menu numérico, escolhendo opções para realizar operações bancárias.

## 📌 Saída
Mensagens informando o status das operações e um extrato detalhado das transações.

## 📌 Exemplo de Uso
Exemplo de interação do usuário:

```
========== BANCO PYTHON ==========
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
Escolha uma opção: 1
Informe o valor do depósito: R$ 500.00
Depósito de R$ 500.00 realizado com sucesso!

========== BANCO PYTHON ==========
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
Escolha uma opção: 2
Informe o valor do saque: R$ 200.00
Saque de R$ 200.00 realizado com sucesso!

========== BANCO PYTHON ==========
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
Escolha uma opção: 3

========== EXTRATO ==========
Depósito: +R$ 500.00
Saque: -R$ 200.00

Saldo atual: R$ 300.00
=============================

========== BANCO PYTHON ==========
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
Escolha uma opção: 4
Saindo do sistema...
```