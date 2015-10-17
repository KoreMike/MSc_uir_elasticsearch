# There is no need to tell this what file to run on!
# i.e. just run 'python edit-citations-metatag.py'

from tempfile import NamedTemporaryFile
from shutil import move
from itertools import groupby

import json

with open("in.txt") as f, NamedTemporaryFile("w", dir=".",delete=False) as out:
    for k, v in groupby(f, key=lambda x: x.lstrip().startswith("{")):
        if not k:
            d = json.loads("{" + "".join(v))
            v = d["metatag.eprints.citation"]
            d["metatag.eprints.citation"] = v[:v.find(")")+1]
            json.dump(d, out)
            out.write("\n")
move(out.name,"in.txt")
