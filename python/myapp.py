import json

def app(environ, start_response):
    data = json.dumps(dict(status='ok', msg='hello'))
    data = data.encode('utf-8')
    start_response("200 OK", [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(data))),
    ])
    return iter([data])
