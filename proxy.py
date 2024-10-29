import click
import requests
import os

from flask import Flask, Response, request
from flask.cli import FlaskGroup

def create_app():
    app = Flask('proxy')

    origin_url = os.getenv("ORIGIN")

    @app.route("/", defaults={"path": ""}, methods=["POST", "GET", "PUT", "PATCH", "UPDATE", "DELETE"])
    @app.route("/<path:path>", methods=["POST", "GET", "PUT", "PATCH", "UPDATE", "DELETE"])
    def proxy(path: str):
        res = requests.request(
            method          = request.method,
            url             = request.url.replace(request.host_url, f'{origin_url}/'),
            headers         = {k:v for k,v in request.headers if k.lower() != 'host'},
            data            = request.get_data(),
            cookies         = request.cookies,
            allow_redirects = False,
        )

        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers          = [
            (k,v) for k,v in res.raw.headers.items()
            if k.lower() not in excluded_headers
        ]

        response = Response(res.content, res.status_code, headers)
        return response
    return app

@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    pass
