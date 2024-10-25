import os
import shutil
from pathlib import Path
from yt_dlp import YoutubeDL
from moviepy.editor import *

# Função responsável pela conversão do MP4 para MP3

def convertMp4ToMp3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

# Função responsável pelo Download e Conversão pelo Youtube

def downloadAndConvertVideoToAudio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': str(Path(os.getcwd()) / f'%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict.get('title', None)
        audio_file_path = Path(os.getcwd()) / f"{info_dict['uploader']} - {video_title}.mp3"
        shutil.move(f"{video_title}.mp3", audio_file_path)

# Adicione o link do YouTube da Música que você deseja Converter para MP3:

youtube_url = "https://www.youtube.com/watch?v=fSHoePrnmMw"

# Chama a função para executar o Download

downloadAndConvertVideoToAudio(youtube_url)