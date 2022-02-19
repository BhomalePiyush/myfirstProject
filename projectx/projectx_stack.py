import aws_cdk
from aws_cdk import (
    # Duration,
    Stack, aws_s3 as _s3
    # aws_sqs as sqs,
)
import boto3
from constructs import Construct

class ProjectxStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, is_prod=False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        _s3.Bucket(self,
                   "myfirstbucket",
                   bucket_name='s3newpiyusbhomale1999',
                   versioned= True,
                   encryption=_s3.BucketEncryption.S3_MANAGED,
                   removal_policy=aws_cdk.RemovalPolicy.DESTROY)   # Destroy S3 when cloud is destroyed if empty
        my_bucket = _s3.Bucket(self,
                               'Mynewbucketpiyushbhomale1999',
                               bucket_name='notcorebucket',
                               removal_policy=aws_cdk.RemovalPolicy.DESTROY)


        #if is_prod:
        #    ProjectxStack=_s3.Bucket(self,
        #                            'MyProdartifactBucket',
        #                             versioned=True,
        #                             encryption=_s3.BucketEncryption.S3_MANAGED)
        #else:
        #   ProjectxStack = _s3(self,
        #                      'myArtificatebucketDevlopment')

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "ProjectxQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
