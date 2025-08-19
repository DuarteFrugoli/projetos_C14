import os
import qrcode

def gerar_qrcode(dados, nome_arquivo, cor_qr="black", cor_fundo="white"):
    # Cria uma instância do QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Adiciona os dados ao QRCode
    qr.add_data(dados)
    qr.make(fit=True)

    # Cria a imagem do QRCode com as cores escolhidas
    img = qr.make_image(fill_color=cor_qr, back_color=cor_fundo)

    # Garante que a pasta 'qrcodes' existe
    pasta = "qrcodes"
    os.makedirs(pasta, exist_ok=True)

    # Garante que o nome do arquivo termina com .png
    if not nome_arquivo.lower().endswith('.png'):
        nome_arquivo += '.png'

    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    # Salva a imagem na pasta 'qrcodes'
    img.save(caminho_arquivo)

