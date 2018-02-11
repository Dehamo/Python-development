from flask import Flask, jsonify, request
import completion
app = Flask(__name__)
completion.load()


@app.route('/', methods=['GET'])
def complete():
    response = ""
    term = request.args['term']
    if term:
        items = completion.candidates(term)
        response = jsonify(items)
        response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    app.run()
