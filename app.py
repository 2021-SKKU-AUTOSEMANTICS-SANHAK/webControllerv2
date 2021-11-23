import json

from flask import Flask, render_template, request, jsonify
from counting.star import stars
app = Flask(__name__)


@app.route('/', methods=['POST'])
def query():
    data = json.loads(request.get_data())
    print(stars())
    return jsonify({"result" : data})

@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
