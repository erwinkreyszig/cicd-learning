from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/operations/add', methods=['GET'])
def perform_addition():
    return jsonify({'result': 'add test'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
