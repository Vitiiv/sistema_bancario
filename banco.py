print('========== BANCO PYTHON ==========')
print(' [1] Depósito\n [2] Saque\n [3] Extrato\n [4] Sair')

opcao = input("Escolha uma opção: ")

valorDeposito = 0.0
saque = 0.0

if opcao == '4':
    print('Saindo do sistema...')
if opcao == '1':
    valorDeposito = float(input('Informe o valor do depósito: R$ '))
    print(f'Depósito de R$ {valorDeposito} realizado com sucesso!')
if opcao == '2':
    saque = float(input('Informe o valor do saque: R$ '))
    print(f'Saque de R$ {saque} realizado com sucesso!')
if opcao == '3':
    print('========== EXTRATO ==========')
    print(f'Depósito: + R$ {valorDeposito}\n'
          f'Saque: - R$ {saque}\n\n'
          f'Saldo atual: R$ {valorDeposito - saque}'
          )