from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

user_list=[]

@app.route('/get_hello', methods=['GET'])
def hello_world():
    return 'Clinton trial successful'

@app.route('/add_user',methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    email = data['email']

    new_user = {"name" : name,
                "email" : email
                }

    user_list.append(new_user)
    return make_response(jsonify({"Message" : "User added successfully", "user name" : new_user['name'] }), 201)

@app.route('/users', methods=['GET'])
def users():
    return make_response(jsonify({"users":user_list,
                                  "status": "Ok"
                                }), 200 )

@app.route('/user/<int:i>', methods=['GET'])
def user(i):
    if len(user_list) <=0:
        return make_response(jsonify({"No users"}))
    se = len(user_list)

    for i in range(se):
        det = user_list[i]
        res = jsonify({"status":200, "data":det})
        return make_response(res)
