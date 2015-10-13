#!/usr/bin/env python

# makes use of script found at:
# http://stackoverflow.com/questions/28953415/removing-duplicate-json-objects-from-file

import json

with open('cleaned-staff-index.json') as f: # change this to match your file name
    # load json objects to dictionaries
    jsons = map(json.loads, f)

# this could be changed to use e.g. 'url' as the unique field
uniques = {x['title']: x for x in jsons}1

# write to new json file
with open('dedup-staff-index.json' ,'w') as nf:
    for js in uniques.values():
        nf.write(json.dumps(js))
        nf.write('\n')

#print uniques.values()
