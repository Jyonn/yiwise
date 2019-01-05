from flask import Flask, request, jsonify, json

app = Flask(__name__)


@app.route('/callback', methods=['GET', 'POST'])
def callback():
    call_id = request.form['call_id']
    print(json.loads(request.form['content'])['words'])
    result = {
        "result": "success",
        "msg": "成功",
        "code": 200,
        "data": {
            "call_id": call_id,
            "action": "play",
            "action_code": "a5a86093-2dec-4992-b2af-8db53e3f8e35.wav",
        }
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
