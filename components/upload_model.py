def upload_model(
    s3_service_name      : str,
    s3_endpoint_url      : str,
    s3_access_key_id     : str,
    s3_secret_access_key : str,
    s3_region            : str,
    s3_bucket            : str
):
    """
    Uploads the model for deployment in the OpenVINO format.

    Parameters:
        - s3_service_name      (str) : The name of the s3 service. It should be 's3'.
        - s3_endpoint_url      (str) : The url of the s3 endpoint.
        - s3_access_key_id     (str) : The access key id for authentication.
        - s3_secret_access_key (str) : The secret access key for authentication.
        - s3_region            (str) : The region where the s3 bucket is located.
        - s3_bucket            (str) : The s3 bucket where the directory will be uploaded.
    """

    import boto3
    import openvino as ov
    import os

    model_directory    = os.path.join('/', 'pipeline', 'artifacts', 'model', 'cats_and_dogs')
    s3_model_directory = os.path.join('models', 'cats_and_dogs', '0')

    ov_model_directory = os.path.join('/', 'tmp', 'model')
    ov_model_file      = os.path.join(ov_model_directory, 'model.xml')

    os.makedirs(ov_model_directory)

    ov_model = ov.convert_model(model_directory, input = ('layer_0_input', [1, 160, 160, 3], ov.Type.f32))
    ov.save_model(ov_model, ov_model_file)

    s3_client = boto3.client(
        service_name          = s3_service_name,
        endpoint_url          = s3_endpoint_url,
        aws_access_key_id     = s3_access_key_id,
        aws_secret_access_key = s3_secret_access_key,
        region_name           = s3_region
    )

    for file in os.listdir(ov_model_directory):

        s3_file = os.path.join(s3_model_directory, file)
        file    = os.path.join(ov_model_directory, file)

        s3_client.upload_file(file, s3_bucket, s3_file)


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    import os
    import subprocess
    import sys

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'boto3==1.34.25'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'openvino==2023.2.0'])

    upload_model(
        s3_service_name      = os.getenv('s3_service_name'),
        s3_endpoint_url      = os.getenv('s3_endpoint_url'),
        s3_access_key_id     = os.getenv('s3_access_key_id'),
        s3_secret_access_key = os.getenv('s3_secret_access_key'),
        s3_region            = os.getenv('s3_region'),
        s3_bucket            = os.getenv('s3_bucket')
    )