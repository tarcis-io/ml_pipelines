def upload_artifacts(
    s3_service_name      : str,
    s3_endpoint_url      : str,
    s3_access_key_id     : str,
    s3_secret_access_key : str,
    s3_region            : str,
    s3_bucket            : str
):
    """
    Uploads the pipeline artifacts to the s3 bucket.

    Parameters:
        - s3_service_name      (str) : The name of the s3 service. It should be 's3'.
        - s3_endpoint_url      (str) : The url of the s3 endpoint.
        - s3_access_key_id     (str) : The access key id for authentication.
        - s3_secret_access_key (str) : The secret access key for authentication.
        - s3_region            (str) : The region where the s3 bucket is located.
        - s3_bucket            (str) : The s3 bucket where the directory will be uploaded.
    """

    import boto3
    import os
    import shutil

    artifacts_directory = os.path.join('/', 'pipeline', 'artifacts')

    file    = shutil.make_archive('artifacts', 'zip', artifacts_directory)
    s3_file = os.path.join('02_model_training', os.path.basename(file))

    s3_client = boto3.client(
        service_name          = s3_service_name,
        endpoint_url          = s3_endpoint_url,
        aws_access_key_id     = s3_access_key_id,
        aws_secret_access_key = s3_secret_access_key,
        region_name           = s3_region
    )

    s3_client.upload_file(file, s3_bucket, s3_file)


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    import os
    import subprocess
    import sys

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'boto3==1.34.28'])

    upload_artifacts(
        s3_service_name      = os.getenv('s3_service_name'),
        s3_endpoint_url      = os.getenv('s3_endpoint_url'),
        s3_access_key_id     = os.getenv('s3_access_key_id'),
        s3_secret_access_key = os.getenv('s3_secret_access_key'),
        s3_region            = os.getenv('s3_region'),
        s3_bucket            = os.getenv('s3_bucket')
    )