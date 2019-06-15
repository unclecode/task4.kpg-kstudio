from flask import Flask, Response, send_from_directory

app = Flask(__name__, static_url_path = '')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  return send_from_directory("index.html")