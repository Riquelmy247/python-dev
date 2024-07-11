from pytube import YouTube
from moviepy.editor import *
import os

print(os.listdir())

diretorio = "./CONVERTER"
diretorio_musica = "./CONVERTIDO"

def baixar_video(url):
    video = YouTube(url)
    video_filename = video.streams.get_highest_resolution().download(filename='musicatemp')
    return video_filename


def converter_para_mp3(video_filename):
    if not os.path.exists(video_filename):
        print(f"O arquivo {video_filename} não foi encontrado.")
        return

    video = VideoFileClip(video_filename)
    audio = video.audio

    youtube = YouTube(url=url_do_video)
    title = youtube.title

    audio_filename = os.path.join(diretorio_musica, f"{title}.mp3")

    audio.write_audiofile(audio_filename)


def remove():
    caminho_arquivo = os.path.join(diretorio, "musicatemp")
    if os.path.isfile(caminho_arquivo):
        os.remove(caminho_arquivo)
        print("O arquivo 'musicatemp' foi removido com sucesso.")
    else:
        print("O arquivo 'musicatemp' não foi encontrado.")


url_do_video = '...'

remove()
video_filename = baixar_video(url_do_video)
converter_para_mp3(video_filename)
