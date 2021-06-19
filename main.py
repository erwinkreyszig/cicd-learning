from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    """
    urls have the following format:
    base_url/endpoint?param=value&param2=value2
      the parts after the question mark is called the query string
      it is composed of key-values separated by &
    the base_url for this application is
      https://turnkey-guild-304701.an.r.appspot.com
    for this method (test) to be executed, someone has to access
    this url using a browser:
    https://turnkey-guild-304701.an.r.appspot.com/test
    ↑ base_url                                    ↑ url endpoint

    the query string part of the url is optional
    if there are query strings provided, like
    base_url/endpoint?param=value&param2=value2
    value and value2 can be accessed from the request.args object

    for example:
    https://turnkey...com/test?color=red&count=3&size=xl
    the query string has three keys: color, count and size
    and each key has a corresponding value:
    color → red
    count → 3
    size → xl
    all values obtained are of string type

    to get the values from request.args, use the following:
      * request.args is a dict type object
    p1 = request.args.get('color')  # p1 will have 'red'
    p2 = request.args.get('count')  # p2 will have '3'
    p3 = request.args.get('size')   # p3 will have 'xl'

    basically any key can be used in the url:
      base_url/stub?a=3&lala=ax&zzz=11
      key   value
      a     3
      lala  ax
      zzz   11
"""
    return jsonify({'result': request.args})


@app.route('/operations/add', methods=['GET'])
def perform_addition():
    return jsonify({'result': 'add test'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
