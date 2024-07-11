from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_video(url, output_path):
    try:
        yt = YouTube(url)

        video_stream = yt.streams.get_highest_resolution()

        video_stream.download(output_path=output_path, filename='video')

        return True
    except Exception as e:
        print("Erro:", e)
        return False


def convert_to_mp3(input_path, output_path):
    try:
        video = VideoFileClip(input_path + 'video.mp4')

        audio = video.audio
        audio.write_audiofile(output_path + 'audio.mp3')

        return True
    except Exception as e:
        print("Erro:", e)
        return False


if __name__ == "__main__":
    youtube_url = "..."
    output_directory = "./CONVERTER"

    if download_video(youtube_url, output_directory):
        if convert_to_mp3(output_directory, output_directory):
            print("Conversão concluída com sucesso!")
        else:
            print("Falha na conversão.")
    else:
        print("Falha no download do vídeo.")
