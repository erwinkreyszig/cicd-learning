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
        return str(e)
    return str(result)


@app.route('/operations/subtract', methods=['GET'])
def perform_subtraction():
    """
    when you type "http://127.0.0.1/operations/subtract?xxx=4,9" on a browser,
    the perform_addition method will be called because the
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


@app.route('/operations/add_or_multiply', methods=['GET'])
def perform_addition_or_multiplication():
    """
    1. check if the key 'op' is in the request.args dictionary
        if it is not there return a message saying you need the 'op' key
        if it is there, get the value for the 'op' key
        1.1. if the value of the 'op' key is not 'add' nor 'multiply',
            output a message that says you don't know that operation
    2. check if the key 'args_from_browser' is in the request.args dictionary
        if it is not there, output a message that says:
            "nothing to add" if the value of 'op' is 'add'
            "nothing to multiply" if the value of 'op' is 'multiply'
        if it is there, get the value because you will need it later
    3. pass the separated items from the 'args_from_browser' and op
        to BasicOperations.add_or_multiply
    """
    print(request.args)
    if 'op' not in request.args:
        return "You need the 'op' key."
    op = request.args.get('op')
    if op != 'add' and op != 'multiply':
        return "I don't know that operation."
    if 'args_from_browser' not in request.args:
        if op == 'add':
            return "Nothing to add"
        else:
            return "Nothing to multiply"
    args_from_browser = request.args.get('args_from_browser')
    split_args = args_from_browser.split(',')
    split_args_list = []
    for something in split_args:
        if something.isnumeric():
            something = int(something)
        split_args_list.append(something)
    result = BasicOperations.add_and_multiply(*split_args_list, op=op)
    print(type(result))
    print(result)
    return str(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
