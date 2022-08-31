from flask import Flask
from flask import jsonify
from flask import request
from flask import json
app = Flask(__name__)
todos = [ { "label": "My first task", "done": False },
        { "label": "My second task", "done": False } ]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    position = int(position)
    del todos[position]
    return jsonify(todos)
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)