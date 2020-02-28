from flask import Response


def flask_response_factory(response):
    web_response = Response(
        response.body,
        status=response.status
    )

    web_response.headers['Content-Type'] = 'application/json'
    web_response.headers['Access-Control-Allow-Origin'] = '*'

    return web_response
