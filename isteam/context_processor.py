from decouple import config


def media_url_root(request):
    bucket_name = config('AWS_STORAGE_BUCKET_NAME')
    if bucket_name:
        return {
            'media_url_root': f'https://{bucket_name}.s3.ap-northeast-2.amazonaws.com/'
        }
