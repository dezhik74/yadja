from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    bucket_name = 'dezhik-yadja'
    location = 'media'


# class StaticStorage(S3Boto3Storage):
#     bucket_name = 'my_bucket'
#     location = 'static'