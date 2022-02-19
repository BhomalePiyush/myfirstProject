import aws_cdk
from aws_cdk import (
    # Duration,
    Stack
    # aws_sqs as sqs,
)
import boto3
from constructs import Construct

class Stackex(Stack):

    def __init__(self, scope: Construct, construct_id: str, is_prod=False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        client = boto3.client('s3')
        clientResponse = client.create_bucket(ACL='public-read-write',
                                              Bucket='piyushbhomalefirstclibucket')
        s3 = boto3.resource('s3')
        BUCKET = "piyushbhomalefirstclibucket"

        s3.Bucket(BUCKET).Object("my-object.py").upload_file("projectx/C-DAC Project/FileToUpload/LogGenerator.py",)