import flask
app = flask.Flask(__name__)

@app.route("/api", methods=['POST'])
def index():
    headers = flask.request.headers
    data = flask.request.data
    return "Request headers:\n" + data.decode('utf-8')

app.run(host="0.0.0.0", port=8080)