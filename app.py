from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Python DevOps Demo API",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/hello/<name>")
def hello(name):
    return jsonify({
        "message": f"Hello, {name}!"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)