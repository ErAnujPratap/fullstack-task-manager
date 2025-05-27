from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = {"id": len(tasks) + 1, "title": data['title'], "completed": False}
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return '', 204

@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def complete_task(task_id):
    for t in tasks:
        if t['id'] == task_id:
            t['completed'] = True
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
