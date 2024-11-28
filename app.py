from flask import Flask, request, jsonify



app = Flask(__name__)

@app.route('/requireWeather', methods=['POST'])
def command_addTask():
    try:
        response_data = {
                        "statusCode": 200,
                        "msg": "获取成功",
                    }

        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"statusCode":500,"msg":f"创建失败:{e}"}), 500


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
