import os
from dotenv import load_dotenv

import logging
import boto3
from botocore.exceptions import ClientError
import os


#Loading environment variables from .env file
load_dotenv()

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def main():
    print(os.getenv('LOGLEVEL'))
    print("hello world")

    source_prefix = os.getenv('SOURCE_PREFIX')
    source_file_name = os.getenv('SOURCE_FILE_NAME')
    dest_bucket = os.getenv('DESTINATION_BUCKET')
    dest_prefix = os.getenv('DESTINATION_PREFIX')
    dest_file_name = os.getenv('DESTINATION_FILE_NAME')
    res = upload_file(source_prefix+'/'+source_file_name, dest_bucket, dest_prefix+'/'+dest_file_name)
    if res is True:
        print("The file is successfully uploaded into s3")


if __name__ == "__main__":
    main()