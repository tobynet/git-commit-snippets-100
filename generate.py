#!/usr/bin/python3

import csv
import json
import os

IN_FILENAME_FOR_SNIPPETS = 'source.txt'
OUT_FILENAME_FOR_VSCODE = os.path.join('out', 'vscode', 'git-commit.json')


def to_vscode_snippet(body: str, prefix: str = None, description: str = None):
    if not prefix:
        prefix = body.split(' ')[0].split('/')[0]
    if not description:
        description = body

    item = {}
    item['prefix'] = prefix.lower()
    item['body'] = body.split('\n')
    item['description'] = description

    return item

def main():
    csv_lines = None
    with open(IN_FILENAME_FOR_SNIPPETS, newline='') as f:
        csv_reader = csv.reader(f, delimiter=',', quotechar='"')
        csv_lines = list(csv_reader)

    snipetts = { s[0]: to_vscode_snippet(s[0]) for s in csv_lines }

    # Debugging
    # print([ x['prefix'] for x in snipetts.values() ])
    #print(json.dumps(snipetts, indent=2))

    with open(OUT_FILENAME_FOR_VSCODE, mode = 'w') as f:
        json.dump(snipetts, f, indent=2)

if __name__ == "__main__":
    main()
