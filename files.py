import json 
from kreuzberg import extract_file_sync, ExtractionConfig
import sqlite3

exampledocx = "exampledocx.docx"

def extract_file(exampledocx):
    fileitems = extract_file_sync(exampledocx, config=ExtractionConfig())
    #print(fileitems)
    filejson =json.dumps(fileitems.content)
    filejson += json.dumps(fileitems.tables)
    with open("filejson", "w") as f:
        f.write(filejson)
    print(filejson)

extract_file(exampledocx)


#now we need to take the json file, clean it with what is needed and upload to the db columns 

# Schema: SQLite
# Table 1 - DEADLINES
# userId, course, deadlineType, weekStart, weekno, hours (that will be learnt over time),


