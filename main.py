import os
import json
from flask import Flask, render_template, request, abort, Response, redirect, jsonify, send_from_directory

app = Flask(__name__, static_folder="/static")

def getProjects():
    with open("testprojects.json","r",encoding="utf-8") as f:
        projects = json.loads(f.read())
    return projects

def addProject(id,title,description,creator,timestamp):
    projects = getProjects()
    projects[str(id)] = {"creator": creator, "title": title, "description": description, "timestamp": int(timestamp), "favorites": 0}
    with open("testprojects.json","w",encoding="utf-8") as f:
        f.write(json.dumps(projects))

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/")
def index():
    return "..."

app.run(host='0.0.0.0', port=80)