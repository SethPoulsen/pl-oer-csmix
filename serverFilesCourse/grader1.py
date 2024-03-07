#! /usr/bin/python3

import json
import pathlib
import os
import glob
import pprint

import sqlitegrader

with open('/grade/data/data.json', 'r') as f:
    data = json.load(f)


sqlitegrader.setup_question(data)

#print(data["partial_scores"])

k = next(iter(data["partial_scores"]))
score = data["partial_scores"][k]["score"]
message = data["partial_scores"][k]["feedback"]
output = data["partial_scores"][k]["output"]

results = {
    "gradable": True,
    "score": score,
    "message": message,
    "output": output,
}

#dir_list = os.listdir('/grade/student/')
#dir_list = glob.iglob('/grade/**/**', recursive=True)

pathlib.Path("/grade/results").mkdir(parents=True, exist_ok=True)
with open('/grade/results/results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f)
