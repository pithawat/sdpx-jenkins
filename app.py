from flask import Flask, request, jsonify

app = Flask(__name__)

# Example route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to my Flask API!"})

# Example GET route
@app.route('/getcode', methods=['GET'])
def hello():
    return jsonify({"message": "hello link"})

@app.route('/plus/<int:x>/<int:y>', methods=['GET'])
def plus(x,y):
    result = x+y
    return jsonify({
        "sum":result
    })
@app.route('/is2hornor/<float:x>', methods=['GET'])
def is_two_hornor(x):
    if x >= 3.25 and x <= 3.49:
        result = True
    else:
        result = False
    return jsonify({
        "gpax": result
    })
        



if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
