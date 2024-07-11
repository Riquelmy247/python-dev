import os

from pytube import YouTube

diretorio = "./CONVERTER"

def baixar_video(url, pasta_destino, qualidade):
    video = YouTube(url)

    stream = video.streams.get_by_resolution(qualidade)

    if stream is None:
        print(f"A qualidade '{qualidade}' não está disponível para este vídeo.")
        return

    nome_arquivo = f"{video.title}_{qualidade}.mp4"

    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

    stream.download(output_path=pasta_destino, filename=nome_arquivo)

    print(f"Vídeo baixado: {caminho_arquivo}")


def remove():
    caminho_arquivo = os.path.join(diretorio, "musicatemp")
    if os.path.isfile(caminho_arquivo):
        os.remove(caminho_arquivo)
        print("O arquivo 'musicatemp' foi removido com sucesso.")
    else:
        print("O arquivo 'musicatemp' não foi encontrado.")


url_do_video = '...'
pasta_destino = './CONVERTIDO'
qualidade_desejada = '720p'

baixar_video(url_do_video, pasta_destino, qualidade_desejada)
remove()
