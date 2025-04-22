import storage
from datetime import datetime

def generate_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def add_task(title, description="", due_date=None):
    tasks = storage.load_tasks()
    
    new_task = {
        'id': generate_id(tasks),
        'title': title,
        'description': description,
        'status': 'Pending',
        'created_at': datetime.now().isoformat()
    }
    
    if due_date:
        new_task['due_date'] = due_date
    
    tasks.append(new_task)
    storage.save_tasks(tasks)
    return new_task

def list_tasks(sort_by_due_date=False):
    all_tasks = storage.load_tasks()
    
    if sort_by_due_date:
        with_dates = []
        without_dates = []
        
        for t in all_tasks:
            if 'due_date' in t:
                with_dates.append(t)
            else:
                without_dates.append(t)
        
        with_dates.sort(key=lambda x: x['due_date'])
        all_tasks = with_dates + without_dates
    
    return all_tasks

def get_task(task_id):
    tasks = storage.load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

def mark_complete(task_id):
    tasks = storage.load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Completed'
            task['completed_at'] = datetime.now().isoformat()
            storage.save_tasks(tasks)
            return True
    return False

def delete_task(task_id):
    tasks = storage.load_tasks()
    initial_len = len(tasks)
    
    tasks = [task for task in tasks if task['id'] != task_id]
    
    if len(tasks) < initial_len:
        storage.save_tasks(tasks)
        return True
    return False 