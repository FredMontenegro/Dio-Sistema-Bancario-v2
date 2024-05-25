def menu():
    menu = '''
    [1] Cadastrar usuario
    [2] Cadastrar conta
    [3] Depositar
    [4] Levantar
    [5] Extrato
    [9] Sair
    \n
    >>>:   
    '''

    return input(menu)


def depositar(valor, saldo, extrato, /):
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: {valor:.2f}€\n'

        else:
            print('Operação não realizada! O valor informado é inválido.')

        return saldo, extrato

        
def sacar(*, valor, saldo, extrato, saque_maximo, quantidade_saques, saque_diario):
        saldo_insuficiente = valor > saldo
        limite_saque = valor > saque_maximo
        limite_diario = quantidade_saques >= saque_diario
        
        

        if saldo_insuficiente:
            print('Operação não realizada! Saldo insuficiente.')

        elif limite_saque:
            print('Operação não realizada! O valor do levantamento excede o limite por operação.')

        elif limite_diario:
            print('Operação não realizada! Número máximo de levantamentos diários atingido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Levantamento: {valor:.2f}€\n'
            quantidade_saques += 1

        else:
            print('Operação não realizada! O valor informado é inválido.')

        return saldo, extrato, quantidade_saques


def exibir_extrato(saldo, /, *, extrato):
        extrato = extrato
        saldo = saldo
        titulo = '  EXTRATO  '
        decorador = '#'

        print(titulo.center(40,'#'))
        print('Nao foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: {saldo:.2f}€')
        print(decorador.center(40,'#'))


def cadastrar_usuario(usuarios):
    nif = input('Informe o NIF: ')
    cadastrado = False
    incluir = {}

    for cliente in usuarios:
        if nif in cliente.values():
            print('Usuário já cadastrado!')
            cadastrado = True

            break

    if not cadastrado:
        incluir['nif'] = nif
        incluir['nome'] = input('Escreva o nome do cliente: ')
        incluir['nascimento'] = input('Informe a data de nascimento (dd-mm-aaaa): ')
        incluir['endereco'] = input('Informe a morada completa: ')

        print('\n\nUsuário cadastrado com sucesso')
        usuarios.append(incluir)


def cadastrar_conta(AGENCIA, guia_conta, usuarios, contas):
    nif = input('Informe o NIF: ')

    cadastrado = True
    incluir = {}

    for cliente in usuarios:
        if nif not in cliente.values():
            print('NIF informado não encontrado!')

            cadastrado = False

            break

    if cadastrado:
        incluir['agencia'] = AGENCIA
        incluir['conta'] = guia_conta
        incluir['nif'] = nif

        print('\n\nConta cadastrada com sucesso')
        contas.append(incluir)


def main():
    SAQUES_DIARIOS = 3
    VALOR_MAXIMO_SAQUE = 500
    AGENCIA = '0001'

    saldo = 0
    extrato = ''
    quantidade_saques = 0
    usuarios = []
    contas = []
    guia_conta = 0

    while True:
        opcao = menu()

        if opcao == '1':
            cadastrar_usuario(usuarios)

        elif opcao == '2':
            guia_conta += 1

            cadastrar_conta(AGENCIA, guia_conta, usuarios, contas)

        elif opcao == '1':
            print(usuarios)

        elif opcao == '2':
            print(contas)

        elif opcao == '3':
            valor = float(input('Informe o valor do deposito: '))
            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == '4':
            valor = float(input('Informe o valor do levantamento: '))
            saldo, extrato, quantidade_saques = sacar(
                valor = valor,
                saldo = saldo,
                extrato = extrato,
                saque_maximo = VALOR_MAXIMO_SAQUE,
                quantidade_saques = quantidade_saques,
                saque_diario = SAQUES_DIARIOS)

        elif opcao == '5':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '9':
            break

        else:
            print('operação inválida, por favor selecione novamente a operação desejada.')

main()