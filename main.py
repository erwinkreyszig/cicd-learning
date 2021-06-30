from flask import Flask, request
from lib.basic_operations import BasicOperations


app = Flask(__name__)


@app.route('/', methods=['GET'])
def default():
    return 'Hello.'


@app.route('/operations/add', methods=['GET'])
def perform_addition():
    # split the value, then check if any of the elements can be turned into 
    # an int, if can, make it an int
    dict_to_find_stuff = request.args
    fetched_value = dict_to_find_stuff.get('args_from_browser')
    split_value = fetched_value.split(',')
    split_values = []
    for x in split_value:
        if x.isnumeric():
            x = int(x)
        split_values.append(x)
    try:
        result = BasicOperations.add(*split_values)
    except Exception as e:
        e = str(e)
        return e
    return str(result)


@app.route('/operations/subtract', methods=['GET'])
def perform_subtraction():
    """
    when you type "http://127.0.0.1/operations/subtract?xxx=4,9" on a browser,
    the perform_addition method will be called beoause the
    "/operations/subtract" from the url matches the one on the
    @app.route('/operations/subtract') part

    to get the "?xxx=4,9" part, this is already in the request.args dictionary
    object, like this:
        request.args = {'xxx': '4,9'} <- '4,9'is a string
                                        * values will always be strings
    everything behind the question mark should be pairs separated by &, the
    pairs are the ones on the left and right side of the equal sign, like this:
        ?fruit=apple&count=7 -> for this, request.args will have
                                {'fruit': 'apple', 'count': '7'}
                                * everything is still a string
        there will also be instances like this:
        ?color=&shape=square -> in this case, request.args will have
                                {'color': '', 'shape': 'square'}
        if there is no question mark after the url, then request.args will be
        an empty dictionary, request.args = {}
    then you need to get the value assigned to the 'args' key from the
    requests.args dictionary:
        value = request.args.get('args') <- after this, value will have '4,9'
    then you can do whatever you want with the contents of value
    """
    # we are expecting at the end of the url something like
    # "?args_from_browser=50,24" (to subtract 24 from 50)
    dict_to_find_stuff = request.args
    # the key 'args_from_browser' was from the browser url
    # fetched_value will have '50,24' <- string
    fetched_value = dict_to_find_stuff.get('args_from_browser')
    # split the contents of variable value
    split_value = fetched_value.split(',')
    # ↑ split_value has ['50', '24']
    # convert elements of variable split_value to int
    split_value_ints = []
    for x in split_value:
        split_value_ints.append(int(x))
    # then we can subtract
    result = BasicOperations.subtract(split_value_ints[0],
                                      split_value_ints[1])
    # lastly return the result
    return str(result)  # string for now


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
