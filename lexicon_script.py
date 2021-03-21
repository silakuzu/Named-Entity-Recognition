#script to retrieve organization, location and person data from 

import re

input_file=open('NER_example_data.txt', encoding="utf8")
file_content = input_file.read()


orgs = re.findall(r'(?<=<b_enamex TYPE="ORGANIZATION">)\w*\s*\w*\s*\w*\s*\w*\s*\w*\s*\w*(?=<e)', file_content)
#print(orgs)

orgs = list(dict.fromkeys(orgs))
with open('all_organizations.txt', 'a', encoding="utf8") as f:
    for item in orgs:
        f.write("\n" + item)


locs = re.findall(r'(?<=<b_enamex TYPE="LOCATION">)\w*\s*\w*\s*\w*\s*\w*\s*\w*\s*\w*(?=<e)', file_content)
locs = list(dict.fromkeys(locs))
with open('all_locations.txt', 'a', encoding="utf8") as f:
    for item in locs:
        f.write("\n" + item)


people = re.findall(r'(?<=<b_enamex TYPE="PERSON">)\w*\s*\w*\s*\w*\s*\w*\s*\w*\s*\w*(?=<e)', file_content)
people = list(dict.fromkeys(people))
with open('all_names.txt', 'a', encoding="utf8") as f:
    for item in people:
        f.write("\n" + item)
