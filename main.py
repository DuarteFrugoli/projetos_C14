from gerador_qrcodes.gerador_qrcode import gerar_qrcode

print('Insira os dados para gerar o QR Code:')
dados = input('Dados: ')
nome_arquivo = input('Nome do arquivo: ')

#insere a cor do fundo do qr code
cor_qr = input('Cor do QR Code (ex: black, blue, red): ')
cor_fundo = input('Cor de fundo (ex: white, yellow): ')

gerar_qrcode(dados, nome_arquivo, cor_qr, cor_fundo)