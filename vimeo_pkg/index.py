import vimeo


def make_upload(token, key, secret, filepath, title, body):
    try:
        v = vimeo.VimeoClient(token, key, secret)

        video_uri = v.upload(
            filepath,
            data={'name': title, 'description': body}
        )

        response = v.patch(video_uri).json()

        return {
            'msg': 'Video uploaded successfully...',
            'link': response["link"],
            'player_embed_url': response["player_embed_url"]
        }

    except FileNotFoundError:
        return 'File path does not exist.'
    except Exception:
        return 'There is an error. Please contact app owners.'
