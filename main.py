from gerador_qrcodes.gerador_qrcode import gerar_qrcode

print('Insira os dados para gerar o QR Code:')
dados = input('Dados: ')
nome_arquivo = input('Nome do arquivo: ')
gerar_qrcode(dados, nome_arquivo)