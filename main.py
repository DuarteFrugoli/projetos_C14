from gerador_qrcodes.gerador_qrcode import gerar_qrcode

while True:
    print('Menu:')
    print('1 - Gerar QR Code')
    print('0 - Encerrar')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print('Insira os dados para gerar o QR Code:')
        dados = input('Dados: ')
        nome_arquivo = input('Nome do arquivo: ')
        try:
            gerar_qrcode(dados, nome_arquivo)
            print(f'QR Code gerado com sucesso: {nome_arquivo}.png')
        except Exception as e:
            print(f'Erro ao gerar QR Code: {e}')
        break
    elif opcao == '0':
        print('Programa encerrado pelo usuário.')
        break
    else:
        print('Opção inválida. Tente novamente.\n')