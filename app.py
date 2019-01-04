from flask import Flask, request

app = Flask(__name__)


@app.route('/callback')
def callback():
    print(request.form)
    print(request.args)
    return ''


if __name__ == '__main__':
    app.run()
