from flask import Flask, Response, request
import requests


app = Flask(__name__)
EXAMPLE_TEST_URL = "https://reddit.com"


@app.route("/", defaults={"path": ""}, methods=["POST", "GET", "PUT", "PATCH", "UPDATE"])
@app.route("/<path:path>", methods=["POST", "GET", "PUT", "PATCH", "UPDATE"])
def proxy(path: str):
    print(request.host_url)
    res = requests.request(
        method          = request.method,
        url             = request.url.replace(request.host_url, f'{EXAMPLE_TEST_URL}/'),
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)