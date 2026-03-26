from flask import FLask
app = Flask(__name__)
@app.route("/")
def home():
    return "CI/CD Working!"
if __name__ == "__main__":
<<<<<<< HEAD
   app.run(host="0.0.0.0", port=5000)
=======
app.run(host="0.0.0.0", port=5000)
>>>>>>> 021683cfcf54a1e27d3db0be59a18fb8c930cc92
