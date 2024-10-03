# Task Tracker

import sys
import json
from collections import defaultdict


def main():
        
    try:
        with open('taskly.json') as f1:
            database = json.load(f1)
    except FileNotFoundError:
        database = {}

    count = len(database)

    if (sys.argv[1] == 'add'):
        in_data = defaultdict(dict)
        in_data['task_id'] = count 
        in_data['description'] = sys.argv[2]
        
        database[count] = in_data
    
    with open('taskly.json','w') as f:
        json.dump(database,f)







main()



