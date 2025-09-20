from flask import Flask, request, jsonify

app = Flask(__name__)

# Example route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to my Flask API!"})

# Example GET route
@app.route('/getcode', methods=['GET'])
def hello():
    return jsonify({"message": "hello"})

@app.route('/plus/<int:x>/<int:y>', methods=['GET'])
def plus(x,y):
    result = x+y
    return jsonify({
        "sum":result
    })

if __name__ == '__main__':
    app.run(debug=True)
