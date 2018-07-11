from flask import Flask


app = Flask(__name__)


@app.route('/')
def main():
    return 'It works!\n'


@app.route('/ping')
def ping():
    return 'Pong\n'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)

