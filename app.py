from flask import Flask, request, jsonify
import profanity

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     if profanity.is_profanity('God damn gurl'):
#         return 'E profanity'
#     else:
#         return 'Nu este profanity'


@app.route('/decide', methods=['POST'])
def is_profanity():
    # if request.content_type != 'application/json':
    #     raise BadRequest('Content-Type has to be application/json')
    req = request.get_json()
    txt = req.get('txt')
    return jsonify(profanity.get_profanity(txt))


@app.route('/prob', methods=['POST'])
def prob():
    # if request.content_type != 'application/json':
    #     raise BadRequest('Content-Type has to be application/json')
    req = request.get_json()
    txt = req.get('txt')
    return jsonify(profanity.get_profanity(txt, prob=True))


if __name__ == '__main__':
    app.run()
