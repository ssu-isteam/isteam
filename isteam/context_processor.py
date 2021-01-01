from decouple import config


def media_url_root(request):
    media_url_root = ''
    try:
        bucket_name = config('AWS_STORAGE_BUCKET_NAME')
        media_url_root = f'https://{bucket_name}.s3.ap-northeast-2.amazonaws.com/'
    except:
        pass

    return {
        'media_url_root': media_url_root
    }
