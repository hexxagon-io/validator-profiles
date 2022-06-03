import re
import glob
import json
import pathlib


EMAIL_REGEX = re.compile(r"[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}")


files = glob.glob("*/*/*.json")
emails = {}

for f in files:
    valAddress = str(pathlib.Path(f).parent.resolve()).split('/')[-1]
    with open(f) as contents:
        for email in EMAIL_REGEX.findall(contents.read()):
            emails[valAddress] = email

with open('validators.json', 'w') as outfile:
    json_string = json.dumps(emails, indent=4, sort_keys=True)
    outfile.write(json_string)
