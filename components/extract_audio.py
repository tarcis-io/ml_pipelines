def extract_audio():
    """
    Extracts the audio from the video.
    """

    import os
    from moviepy.editor import VideoFileClip

    artifacts_directory = os.path.join('/', 'pipeline', 'artifacts')
    video_file          = os.path.join(artifacts_directory, 'video.mp4')
    video_audio_file    = os.path.join(artifacts_directory, 'video_audio.mp3')

    video_file_clip = VideoFileClip(video_file)
    video_file_clip.audio.write_audiofile(video_audio_file)


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    import subprocess
    import sys

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'moviepy==1.0.3'])

    extract_audio()