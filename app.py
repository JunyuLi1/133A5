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


@app.route('/loadTask', methods=['GET'])
def command_loadNoteTask():
    try:
        username = request.args.get("username")
        result = databse.load_note(username)
        if result:
            response_data = {
                            "statusCode": 200,
                            "success": True,
                            "note": result
                        }
            return jsonify(response_data), 200
        else:
            response_data = {
                            "statusCode": 400,
                            "message": "No such user, please sign up"
                        }
            return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"statusCode":500,"success": False, "message": str(e)}), 500

@app.route('/insertTask', methods=['POST'])
def command_insertNoteTask():
    try:
        data = request.get_json()
        username = data.get("username")
        time = data.get("time")
        description = data.get("description")
        category = data.get("category")
        result = databse.insert_note(username, time, description, category)
        if result:
            response_data = {
                            "statusCode": 200,
                            "success": True
                        }
            return jsonify(response_data), 200
        else:
            response_data = {
                            "statusCode": 400,
                            "message": "No such user, please sign up"
                        }
            return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"statusCode":500,"success": False, "message": str(e)}), 500

@app.route('/editTask', methods=['POST'])
def command_editNoteTask():
    try:
        data = request.get_json()
        id = data.get("id")
        username = data.get("username")
        time = data.get("time")
        description = data.get("description")
        category = data.get("category")
        result = databse.edit_note(id, username, time, description, category)
        if result:
            response_data = {
                            "statusCode": 200,
                            "success": True
                        }
            return jsonify(response_data), 200
        else:
            response_data = {
                            "statusCode": 400,
                            "message": "No such user, please sign up"
                        }
            return jsonify(response_data), 200
    except Exception as e:
        print(e)
        return jsonify({"statusCode":500,"success": False, "message": str(e)}), 500
    
@app.route('/deleteTask', methods = ['POST'])
def command_deleteNote():
    try:

        data = request.get_json()
        id = data.get("id")
        result = databse.delete_note(id)
        if result:
            response_data = {
                            "statusCode": 200,
                            "success": True
                        }
            return jsonify(response_data), 200
        else:
            response_data = {
                            "statusCode": 400,
                            "message": "Fail to delete"
                        }
            return jsonify(response_data), 200

    except Exception as e:
        print(e)
        return jsonify({"statusCode":500,"success": False, "message": str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)
