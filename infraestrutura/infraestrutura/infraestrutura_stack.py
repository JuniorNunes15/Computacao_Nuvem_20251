from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_s3_deployment as s3deploy,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
)
from constructs import Construct

class InfraestruturaStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        site_bucket = s3.Bucket(self, "SiteBucket",
                                website_index_document="index.html",
                                public_read_access=True)

        s3deploy.BucketDeployment(self, "DeployReactSite",
            sources=[s3deploy.Source.asset("../frontend/build")],
            destination_bucket=site_bucket)

        backend_lambda = _lambda.Function(self, "FlaskBackend",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="app.lambda_handler",
            code=_lambda.Code.from_asset("../backend"))

        apigateway.LambdaRestApi(self, "FlaskAPI", handler=backend_lambda)

        cloudfront.CloudFrontWebDistribution(self, "SiteCDN",
            origin_configs=[
                cloudfront.SourceConfiguration(
                    s3_origin_source=cloudfront.S3OriginConfig(
                        s3_bucket_source=site_bucket
                    ),
                    behaviors=[cloudfront.Behavior(is_default_behavior=True)]
                )
            ])
