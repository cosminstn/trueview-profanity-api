from textblob import TextBlob
from profanity_check import predict, predict_prob
from flask import Flask


ro = TextBlob("Toate peste toate smartphone-ul are specificatii de tot, aproape toate componentele fiind high end, "
              "mai putin display-ul")
en = TextBlob("Waiting for this laptop and all the rumors were very exciting, but instead Apple has offered us this "
              "piece of shit")
print(ro.detect_language())
print(en.detect_language())

print('Profanity checking: ')
print(predict(['fu ck it bro']))


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
