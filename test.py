import flask
app = flask.Flask(__name__)

@app.route("/")
def index():
    headers = flask.request.headers
    return "Request headers:\n" + headers['slatt']

app.run(host="0.0.0.0", port=8080)