from aws_cdk import (
    # Duration,
    Stack, aws_s3 as _s3
    # aws_sqs as sqs,
)
from constructs import Construct

class ProjectxStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        _s3.Bucket(self,
                   "myfirstbucket",
                   bucket_name='s3newpiyusbhomale1999',
                   versioned= True,
                   encryption=_s3.BucketEncryption.S3_MANAGED,
                   block_public_access=_s3.BlockPublicAccess.BLOCK_ALL)
        my_bucket = _s3.Bucket(self,
                               'Mynewbucketpiyushbhomale1999',
                               bucket_name='notcorebucket')



        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "ProjectxQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
