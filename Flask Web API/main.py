from flask import Flask, request, jsonify
from DatabaseManager import DatabaseManager, convert_to_json_serializable
from datetime import datetime

app = Flask(__name__)
database = DatabaseManager()

@app.route('/tasks', methods=['POST'])
def add_new_task():
    data = request.json
    task_name = data.get('title')
    description = data.get('description')
    due_date = data.get('due_date')
    priority = data.get('priority')

    if not task_name or not description or not due_date or not priority:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        datetime.strptime(due_date, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        return jsonify({"error": "Invalid date format. Please enter the date in ISO format."}), 400

    task = {"task_id": None, "title": task_name, "description": description, "due_date": due_date, "priority": priority, "status": "pending"}
    try:
        database.add_task(task)
        return jsonify({"message": "Task added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    update_data = {}

    if 'description' in data:
        update_data['description'] = data['description']
    if 'due_date' in data:
        try:
            datetime.strptime(data['due_date'], "%Y-%m-%dT%H:%M:%S")
            update_data['due_date'] = data['due_date']
        except ValueError:
            return jsonify({"error": "Invalid date format. Please enter the date in ISO format."}), 400
    if 'priority' in data:
        update_data['priority'] = data['priority']
    if 'status' in data:
        update_data['status'] = data['status']

    if not update_data:
        return jsonify({"error": "No valid fields to update"}), 400

    modified = database.update_task(task_id, update_data)
    if modified:
        return jsonify({"message": "Task updated successfully!"}), 200
    else:
        return jsonify({"message": "No changes made."}), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    deleted_count = database.delete_task(task_id)
    if deleted_count > 0:
        return jsonify({"message": "Task removed successfully!"}), 200
    else:
        return jsonify({"message": "Task not found."}), 404

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = database.get_all_task()
    if not tasks:
        return jsonify({"message": "No tasks found."}), 404
    else:
        return jsonify(convert_to_json_serializable(tasks)), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_specific_task(task_id):
    task = database.check_task_exists(task_id)
    if not task:
        return jsonify({"message": "Task does not exist!"}), 404
    else:
        return jsonify(convert_to_json_serializable(task)), 200

if __name__ == '__main__':
    app.run(debug=True)