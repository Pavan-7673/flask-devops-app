from flask import Flask, make_response
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
@app.route("/")
def home():
    response = make_response("Hello from backend 🚀")
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
