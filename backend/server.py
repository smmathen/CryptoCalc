from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({})

@app.route("/api/modexp")
def about():
    return jsonify({})

@app.route("/api/euclideanalgo")
def about():
    return jsonify({})




if __name__ == '__main__':
    app.run(debug=True)