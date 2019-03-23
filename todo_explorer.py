from lib import prepare_files, prepare_tree
import json
from datetime import datetime as dt
from pathlib import Path

TODOS = {}
KEY = '@TODO'

print(dt.now())

files = prepare_files( prepare_tree() )
todo_count = 0
file_id = 1

for f in files:
    current_filename = f.name.replace('\\', '/' , -1) # WINDOWS !!!
    TODOS[str(file_id)] = {}
    TODOS[str(file_id)]["file_path"] = current_filename
    TODOS[str(file_id)]["contents"] = {}

    try:
        for lix, line in enumerate(f.readlines()):
            if KEY in line:
                TODOS[str(file_id)]["contents"][lix+1] = line
                todo_count += 1     
    except UnicodeDecodeError as e:
        print(e)
        continue

    if len(TODOS[str(file_id)]["contents"].keys()) == 0:
        del TODOS[str(file_id)]

    file_id += 1
    f.close()

res_f_name = 'results_' + dt.isoformat(dt.now())[:-7].replace(":","-", -1).replace("T", "_") + '.json'

results = open(res_f_name, 'x')
results.write(json.dumps(TODOS, indent=2, sort_keys=False))

results.close()

# print(json.dumps(TODOS, indent=2), '\n\n', 'found: ', todo_count, "ToDos", "in", len(TODOS.keys()), "files")

'''
    PATH CONVERSION: Pathlib,
    Path("C:/Users/marcin.danlowski/GIT/TODOExplorer/test/test nested/test.txt")
'''