from decouple import config
from vimeo_pkg.index import make_upload

def upload():
    try:
        key = config('CLIENT_ID')
        token = config('ACCESS_TOKEN')
        secret = config('CLIENT_SECRET')
        filepath = config('FILE_PATH')
        title = input('Enter video title\n')
        body = input('Enter short video description\n')

        return make_upload(token, key, secret, filepath, title, body)

    except Exception:
      return 'Credentials not found.'
