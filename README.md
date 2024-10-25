# MP3 Converter With Python

Este script em Python permite que você baixe vídeos do YouTube como arquivos de áudio MP3.

## Funcionalidades

1. **Baixar e Converter Vídeo para Áudio:**
   - Função: `downloadAndConvertVideoToAudio(youtube_url)`
   - Baixa um vídeo do YouTube a partir da URL informada, converte-o para MP3 e salva dentro do repositório utilizado.
   -  Parâmetros:
     - `url` (str): Link do vídeo dentro do YouTube.

2. **Converter MP4 para MP3**
   - Função: `convertMp4ToMp3(mp4, mp3)`
   - Converte um arquivo MP4 para o formato MP3.
   - Parâmetros:
     - `mp4` (str): Caminho do arquivo MP4 de entrada.
     - `mp3` (str): Caminho para salvar o arquivo MP3 de saída.

## Uso

1. Clone este repositório para sua máquina local.
2. Instale as dependências necessárias (`yt_dlp`, `moviepy`, `pathlib`).
3. Execute o script.

## Observações

- O script baixa o áudio na melhor qualidade disponível (140).
- Os arquivos MP4 baixados são excluídos após a conversão para economizar espaço em disco.
- Certifique-se de baixar e atualizar as bibliotecas necessárias e incluir os endereços necessários no PATH das configurações avançadas do Sistema.

## Aviso Legal

Este script destina-se apenas para uso pessoal. Certifique-se de ter os direitos necessários para baixar e usar o conteúdo antes de prosseguir.
