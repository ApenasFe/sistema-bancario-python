#Criar um sistema bancário com operações de saque, deposito e visualização de extrato.

saldo_total = 0
extrato_dict = {}

saque_contagem = 0
deposito_contagem = 0

#Operação de depósito
def operacao_deposito():
    while True:
        try:
            string_deposito = input('Digite a quantia à ser depositado: \n')
            deposito_formatado = string_deposito.replace(".", "")
            if deposito_formatado.isnumeric() == True:
                valor_deposito = float(string_deposito)
                break
            else:
                raise ValueError
        except ValueError:
            print('Opção inválida')
    print(f'Foi depositado R$ {valor_deposito} para sua conta')

    def armazenar_transacao(valor, transacao, numero_transacao):
        transacao["Deposito" + f'{numero_transacao}'] = valor
    armazenar_transacao(valor=valor_deposito, transacao=extrato_dict, numero_transacao=deposito_contagem)
    
    return valor_deposito

#Operação de saque
def operacao_saque(saldo):
    def armazenar_transacao(valor, transacao, numero_transacao):
        transacao["Saque" + f"{numero_transacao}"] = -valor
    
    while True:
        try:
            string_saque = input('Digite a quantia à ser retirado: \n')
            saque_formatado = string_saque.replace(".", "")
            if saque_formatado.isnumeric() == True:
                valor_saque = float(string_saque)
                break
            else:
                raise ValueError
        except ValueError:
            print('Opção inválida')
        
    if valor_saque <= saldo:
        armazenar_transacao(valor=valor_saque, transacao=extrato_dict, numero_transacao=saque_contagem)
        return valor_saque
    else:
        print('Não foi possível efetuar a transação. Saldo insuficiente.')
        return 0
        

#Operação de extrato
def operacao_extrato(extrato, saldo):
    print(f'Saldo: R$ {saldo}')
    for transacao in extrato:
        print(f'{transacao}: {extrato[transacao]}')

#Menu
while True:
    print(f'Saldo atual: R$ {saldo_total}')
    opcao_do_usuario = input('Digite "d" para depositar, "s" para sacar, "e" para visualizar o extrato ou "q" para sair... \n').lower()

    match opcao_do_usuario:
        case 'd':
            print('Deposito selecionado')
            valor_depositado = operacao_deposito()
            saldo_total += valor_depositado
            deposito_contagem += 1
        case 's':
            print('Saque selecionado')
            valor_sacado = operacao_saque(saldo_total)
            saldo_total -= valor_sacado
            saque_contagem += 1
        case 'e':
            print('Extrato bancário:')
            operacao_extrato(extrato=extrato_dict, saldo=saldo_total)
        case 'q':
            print('Encerrar o programa')
            break
        case _:
            print('Opção inválida')