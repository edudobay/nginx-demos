import json

async def app(scope, receive, send):
    assert scope['type'] == 'http'

    data = json.dumps(dict(status='ok', msg='hello'))
    data = data.encode('utf-8')

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            (b"Content-Type", b"application/json"),
            (b"Content-Length", b'%d' % len(data)),
        ],
    })

    await send({
        'type': 'http.response.body',
        'body': data,
    })
