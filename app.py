from flask import Flask, request, jsonify
from flask_cors import CORS
from tools import OpenWeather as op
from db import database as databse


app = Flask(__name__)
CORS(app)
weatherObj = op.OpenWeather()

@app.route('/requireWeather', methods=['GET'])
def command_addTask():
    try:
        data = weatherObj._download_url(weatherObj.url)
        if data is not None:
            data = data['weather'][0]['description']
        else:
            raise Exception("Cannot query Weather data, please try again.")
        response_data = {
                        "statusCode": 200,
                        "msg": "Success",
                        "data": data
                    }
        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"statusCode":500,"msg":f"Failed:{e}"}), 500

@app.route('/login', methods=['POST'])
def command_loginUser():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        result = databse.request_user(username, password)
        if result:
            response_data = {
                            "statusCode": 200,
                            "success": True
                        }
            return jsonify(response_data), 200
        else:
            response_data = {
                            "statusCode": 400,
                            "success": False,
                            "message": "No such user, please sign up"
                        }
            return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"statusCode":500,"success": False, "message": str(e)}), 500


@app.route('/register', methods=['POST'])
def command_registUser():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        result = databse.register_user(username, password)
        if result:
            response_data = {
                            "statusCode": 200,
                            "success": True
                        }
            return jsonify(response_data), 200
        else:
            response_data = {
                            "statusCode": 400,
                            "success": False,
                            "message": "Already exist!"
                        }
        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"statusCode":500,"success": False, "message": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)
