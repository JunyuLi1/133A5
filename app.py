from flask import Flask, request, jsonify
from flask_cors import CORS
from tools import OpenWeather as op



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


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
