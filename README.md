# Projeto Gerador de QR Code

Este é um projeto simples desenvolvido para a aula de C14 no Inatel. O objetivo é aprender sobre o versionamento de código e gerenciamento de dependências. Para isso criamos código que gera um QR Code a partir de um link (URL) fornecido pelo usuário.

## Funcionalidade

- Gera um QR Code a partir de qualquer URL informada.

## Como usar

1. Informe o link (URL) desejado
2. Informe o nome do arquivo. Ele será gerado no formato .png, não é necessário informar o seu tipo (extensões de nomes de arquivos).
2. informe as cores desejadas para o qrcode.
2. O sistema irá gerar e exibir o QR Code correspondente em uma pasta separada.

## Como configurar, instalar dependências e executar o projeto

Siga os passos abaixo para rodar o projeto utilizando o Poetry:

1. **Instale o Poetry**  
   Caso ainda não tenha o Poetry instalado, execute o comando abaixo no terminal:
   ```sh
   pip install poetry
   ```

2. **Clone o repositório**  
   Baixe o projeto para sua máquina:
   ```sh
   git clone https://github.com/DuarteFrugoli/projetos_C14.git
   cd C14_dependecias
   ```

3. **Instale as dependências**  
   O Poetry irá instalar todas as dependências listadas no arquivo [`pyproject.toml`](pyproject.toml):
   ```sh
   poetry install
   ```

4. **Ative o ambiente virtual do Poetry**  
   Para garantir que os comandos sejam executados no ambiente correto:
   ```sh
   poetry shell
   ```

5. **Execute o projeto**  
   Rode o arquivo principal para iniciar o gerador de QR Codes:
   ```sh
   python main.py
   ```

Pronto! Agora basta seguir as instruções exibidas no terminal para gerar seus QR codes.