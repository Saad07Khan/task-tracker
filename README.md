# Task Tracker

Hey there! This is my implementation of a simple task tracker command-line app.

## What it does

- Add tasks with titles and descriptions
- Set due dates if you want (totally optional)
- List all your tasks 
- Mark things as done when you finish them
- Delete tasks you don't need anymore
- Sorts by due date if you want
- Saves everything to a JSON file

## Setup

You'll need Python 3.6+ to run this. Just download the files and you're good to go!

## How to use it

### Adding a task

```
python main.py add "Finish homework" -d "Math problems on page 32" --due 2023-12-31
```

### Listing tasks

```
python main.py list
```

Want to sort by due date? Just add `--sort-by-due`:

```
python main.py list --sort-by-due
```

### Mark a task complete

```
python main.py complete 1
```

### Delete a task

```
python main.py delete 1
```

### Need help?

```
python main.py --help
```

## Project files

- main.py - The main program
- task_manager.py - Task management functions
- storage.py - Handles saving/loading data
- tasks.json - Where your tasks are stored

## Issues I ran into

Had some trouble with the date sorting, especially when some tasks have due dates and others don't. Also making sure the interface was easy to use took some thinking.

Feel free to use this however you want! 