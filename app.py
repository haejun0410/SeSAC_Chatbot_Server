from flask import Flask,jsonify,request
import chatbot
import sys,json
import random
application = Flask(__name__)

@application.route("/")
def hello():
    return "hello"

@application.route("/preg_help", methods = ["POST"])
def return_response():
    request_data = json.loads(request.get_data(),encoding="utf-8")
    user_input = request_data['userRequest']['utterance']
    print("Requested Data : {}".format(user_input))
    answer = chatbot.chatbot_response(user_input)
    response = {
        "version" : "2.0",
        "template" : {
            "outputs" : [
                {
                    "simpleText" : {
                        "text" : answer
                    }
                }
            ]
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    application.run(host = "0.0.0.0", port = int(sys.argv[1]), debug = True)