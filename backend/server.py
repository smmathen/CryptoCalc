from flask import Flask, jsonify, request

app = Flask(__name__)
def EA(a,b):
    if(b>a):
        return EA(b,a)
    elif(a%b==0):
        return b
    else:
        return EA(b,a%b)
@app.route("/")
def home():
    return jsonify({})

@app.route("/api/modexp")
def modexp():
    data = request.args
    return jsonify({ans: pow(data.get("base"), data.get("exp"), data.get("mod"))})

@app.route("/api/euclideanalgo")
def EeuclidAlgo():
    data = request.args
    return jsonify({ans: EA(data.get("a"), data.get("b"))})




if __name__ == '__main__':
    app.run(debug=True)