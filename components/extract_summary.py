def extract_summary():
    """
    Extracts the summary from the video.
    """

    import os
    from transformers import pipeline

    artifacts_directory = os.path.join('/', 'pipeline', 'artifacts')
    video_speeches_file = os.path.join(artifacts_directory, 'video_speeches.txt')
    video_summary_file  = os.path.join(artifacts_directory, 'video_summary.txt')

    with open(video_speeches_file, 'r') as file:

        speeches = file.read()

    pipe    = pipeline(task = 'summarization', model = 'sshleifer/distilbart-cnn-12-6')
    summary = pipe(speeches)

    with open(video_summary_file, 'w') as file:

        file.write(summary[0]['summary_text'])


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    import subprocess
    import sys

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'torch==2.1.2'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'transformers==4.37.1'])

    extract_summary()