#!/usr/bin/env python3
import argparse
import task_manager
from datetime import datetime

def format_task(task):
    result = f"ID: {task['id']} | Title: {task['title']} | Status: {task['status']}"
    
    if task['description']:
        result += f"\n   Description: {task['description']}"
    
    if 'due_date' in task:
        result += f"\n   Due Date: {task['due_date']}"
    
    return result

def main():
    parser = argparse.ArgumentParser(description='Task Tracker CLI')
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', help='Task title')
    add_parser.add_argument('-d', '--description', help='Task description')
    add_parser.add_argument('--due', help='Due date (YYYY-MM-DD)')
    
    list_parser = subparsers.add_parser('list', help='List all tasks')
    list_parser.add_argument('--sort-by-due', action='store_true', help='Sort tasks by due date')
    
    complete_parser = subparsers.add_parser('complete', help='Mark a task as completed')
    complete_parser.add_argument('id', type=int, help='Task ID to mark as completed')
    
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task ID to delete')
    
    args = parser.parse_args()
    
    if args.command == 'add':
        due = None
        if args.due:
            try:
                due = datetime.strptime(args.due, '%Y-%m-%d').strftime('%Y-%m-%d')
            except ValueError:
                print("Error: Due date must be in YYYY-MM-DD format")
                return
        
        new_task = task_manager.add_task(args.title, args.description or "", due)
        print(f"Task added successfully with ID: {new_task['id']}")
    
    elif args.command == 'list':
        print("Debug: Getting tasks...")
        all_tasks = task_manager.list_tasks(sort_by_due_date=args.sort_by_due)
        print(f"Debug: Got {len(all_tasks)} tasks")
        if not all_tasks:
            print("No tasks found")
            return
        
        print("Tasks:")
        for t in all_tasks:
            print(format_task(t))
            print("-" * 40)
    
    elif args.command == 'complete':
        if task_manager.mark_complete(args.id):
            print(f"Task {args.id} marked as completed")
        else:
            print(f"Task with ID {args.id} not found")
    
    elif args.command == 'delete':
        if task_manager.delete_task(args.id):
            print(f"Task {args.id} deleted successfully")
        else:
            print(f"Task with ID {args.id} not found")
    
    else:
        parser.print_help()

if __name__ == '__main__':
    main() 