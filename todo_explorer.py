from lib import prepare_files, prepare_tree
import json
from datetime import datetime as dt

TODOS = {}
KEY = '@TODO'

print(dt.now())

files = prepare_files( prepare_tree() )
todo_count = 0

for f in files:
    current_filename = f.name
    TODOS[current_filename] = {}

    try:
        for lix, line in enumerate(f.readlines()):
            if KEY in line:
                TODOS[current_filename][lix+1] = line
                todo_count += 1     
    except UnicodeDecodeError as e:
        print(e)
        continue

    if len(TODOS[current_filename].keys()) == 0:
        del TODOS[current_filename]
    
    f.close()



print(json.dumps(TODOS, indent=2), '\n\n', 'found: ', todo_count, "ToDos", "in", len(TODOS.keys()), "files")