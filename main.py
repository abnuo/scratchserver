from flask import Flask, render_template, request, abort, Response, redirect, jsonify, send_from_directory

app = Flask(__name__, static_folder="/static")

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/")
def index():
    return "..."

app.run(host='0.0.0.0', port=80)