def extract_speeches():
    """
    Extracts the speeches from the video.
    """

    import os
    import tarfile
    import urllib.request

    from transformers import pipeline

    ffmpeg_url  = 'https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz'
    ffmpeg_file = os.path.basename(ffmpeg_url)

    urllib.request.urlretrieve(ffmpeg_url, ffmpeg_file)

    with tarfile.open(ffmpeg_file) as ffmpeg_tarfile:

        ffmpeg_tarfile.extractall()

    for directory in next(os.walk('.'))[1]:

        if directory.startswith('ffmpeg'):

            ffmpeg_directory = os.path.join(os.getcwd(), directory)
            break

    os.environ['PATH'] += os.pathsep + ffmpeg_directory

    artifacts_directory = os.path.join('/', 'pipeline', 'artifacts')
    video_audio_file    = os.path.join(artifacts_directory, 'video_audio.mp3')
    video_speeches_file = os.path.join(artifacts_directory, 'video_speeches.txt')

    pipe     = pipeline(task = 'automatic-speech-recognition', model = 'openai/whisper-tiny')
    speeches = pipe(video_audio_file)

    with open(video_speeches_file, 'w') as file:

        file.write(speeches['text'])


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    import subprocess
    import sys

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'torch==2.1.2'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'transformers==4.37.1'])

    extract_speeches()