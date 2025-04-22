import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    print("Debug: Loading tasks...")
    if not os.path.exists(TASKS_FILE):
        print("Debug: Tasks file doesn't exist")
        return []
    
    try:
        file = open(TASKS_FILE, 'r')
        data = json.load(file)
        file.close()
        print(f"Debug: Loaded {len(data)} tasks")
        return data
    except json.JSONDecodeError:
        print("Debug: JSON decode error")
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4) 