from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

app = Flask(__name__)

def download_youtube_video(url, output_path):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(file_extension='mp4', progressive=True).first()
        video_stream.download(output_path)
        print("Download concluído!")
    except Exception as e:
        print("Ocorreu um erro:", str(e))

def convert_mp4_to_mp3(input_file, output_file):
    video_clip = VideoFileClip(input_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_file, codec='mp3')
    audio_clip.close()
    video_clip.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        output_directory = "./downloads/"
        download_youtube_video(url, output_directory)

        lista_arquivos = os.listdir(output_directory)
        lista_datas = []
        for arquivo in lista_arquivos:
            if ".mp4" in arquivo:
                data = os.path.getmtime(f"{output_directory}/{arquivo}")
                lista_datas.append((data, arquivo))

        lista_datas.sort(reverse=True)
        ultimo_arquivo = lista_datas[0]
        arquivo, extensao = os.path.splitext(ultimo_arquivo[1])

        input_file = "downloads/" + arquivo + ".mp4"
        output_file = "downloads/" + arquivo + ".mp3"
        convert_mp4_to_mp3(input_file, output_file)
        os.remove("downloads/" + arquivo + ".mp4")
        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)