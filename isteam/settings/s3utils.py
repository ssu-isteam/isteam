from storages.backends.s3boto3 import S3Boto3Storage
from decouple import config

StaticRootS3BotoStorage = lambda: S3Boto3Storage(location=config('STATIC_PATH'))
MediaRootS3BotoStorage = lambda: S3Boto3Storage(location=config('MEDIA_PATH'))