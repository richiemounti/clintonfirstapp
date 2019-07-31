from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

user_list=[]

@app.route('/get_hello', methods=['GET'])
def hello_world():
    return 'Clinton trial successful'


'''
creates a new user and adds it to the user_list
'''
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

'''
gets all users in the list
'''
@app.route('/users', methods=['GET'])
def users():
    return make_response(jsonify({"users":user_list,
                                  "status": "Ok"
                                }), 200 )

'''
gets a specific user based on the position in the list
'''
@app.route('/user/<int:i>', methods=['GET'])
def user(i):
    if len(user_list) <=0:
        return make_response(jsonify({"No users"}))
    se = len(user_list)

    if i in range(se):
        det = user_list[i]
        res = jsonify({"status":200, "data":det})
        return make_response(res)

'''
deletes a user
'''
@app.route('/user/<int:i>', methods=['DELETE'])
def delete_user(i):
    if len(user_list) <= 0:
        return make_response(jsonify({"Cannot delete user. Id {} does not exist"}))
    se = len(user_list)
    if i in range(se):
        del user_list[i]

        return make_response(jsonify({"status":200, "data":"User {} deleted".format(i)}))

'''
updates user credentials
'''
@app.route('/user/<int:i>', methods=['PATCH'])
def update_user(i):
    data = request.get_json()
    if i in range(len(user_list)):
        user_list[i] = {"name": data['name'], "email": data['email']}
        res = jsonify({"status":202, "data": user_list[i]})
        return make_response(res, 202)
    res = jsonify({"status": 404, "error": "User with id {} not found".format(i)})
    return make_response(res, 404)