from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/operations/add', methods=['GET'])
def perform_addition():
    return jsonify({'result': 'add test'})


@app.route('/operations/subtract', methods=['GET'])
def perform_addition():
    # we are expecting ?args=50,24 (subtract 24 from 50)
    args = request.args  # this is a dict (but you cannot edit this)
    # since we are expecting args, we know that there will be
    # a key called 'args'
    value = args.get('args')  # value now has the string '50,24'
    # split the contents of variable value
    split_value = value.split(',')  # split_value has ['50', '24']
    # convert elements of variable split_value to int
    split_value_ints = []
    for x in split_value:
        split_value_ints.append(int(x))
    # then we can subtract
    result = split_value_ints[0] - split_value_ints[1]
    # lastly return the result
    return result


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
