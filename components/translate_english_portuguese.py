def translate_english_portuguese():
    """
    Translates the summary of the video to portuguese.
    """

    import os
    from transformers import pipeline

    artifacts_directory           = os.path.join('/', 'pipeline', 'artifacts')
    video_summary_file            = os.path.join(artifacts_directory, 'video_summary.txt')
    video_summary_portuguese_file = os.path.join(artifacts_directory, 'video_summary_portuguese.txt')

    with open(video_summary_file, 'r') as file:

        speeches = file.read()

    pipe        = pipeline(task = 'translation', model = 'unicamp-dl/translation-en-pt-t5')
    translation = pipe(speeches)

    with open(video_summary_portuguese_file, 'w') as file:

        file.write(translation[0]['translation_text'])


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    import subprocess
    import sys

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'torch==2.1.2'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'transformers==4.37.1'])

    translate_english_portuguese()