"""Reading and writing the Archive file.

YOU IMPLEMENT THIS FILE.

The file format is CSV with no header row. One record per line, five fields
separated by commas, in this order:

    id,title,city,year,condition
    MS001,Tarikh al-Sudan,Timbuktu,1655,fragile

Remember Session 1: a file is one long line of characters. The comma
separates fields; the newline separates records. Nothing else is doing
any work.
"""

from archive.errors import MalformedRecordError
from archive.validation import validate_record

FIELD_NAMES = ["id", "title", "city", "year", "condition"]


def parse_line(line):
    """Turn one CSV line into a dict with the five FIELD_NAMES as keys.

    Whitespace around the line (including the trailing newline) is stripped.
    Field values are stripped too.

    If the line does not split into exactly 5 fields, raise
    MalformedRecordError. Do not guess, do not pad with blanks — a line with
    four fields is not a record with an empty one, it is a broken line, and
    the difference matters when you report it to whoever typed it.

    Returns dict.
    """
    EmptyDict = {}
    s = ""
    prev_comma = 0
    line = line.rstrip("\n")   # the newline is a record separator, not data
    for i in range(len(line)):
        if line[i] == ',':
            prev_comma += 1
            if prev_comma == 1:
                EmptyDict["id"] = s
                s = ""
            elif prev_comma == 2:
                EmptyDict["title"] = s
                s = ""
            elif prev_comma == 3:
                EmptyDict["city"] = s
                s = ""
            elif prev_comma == 4:
                EmptyDict["year"] = s
                s = ""
            else:
                raise MalformedRecordError("parse_line")
        else:
            s += line[i]

    if prev_comma != 4:
        raise MalformedRecordError("parse_line")

    EmptyDict["condition"] = s
    return EmptyDict

        


def load_archive(path):
    """Read the file at `path` and return (valid_records, rejected_lines).

    valid_records   list of dicts that passed validate_record
    rejected_lines  list of the ORIGINAL line strings that did not — either
                    because they were malformed, or because validation
                    rejected them

    A file that does not exist is not an error. It means the archive is new.
    Return ([], []) and DO NOT raise. Your program must start on a machine
    where nobody has saved anything yet.

    Blank lines are skipped silently.

    Returns (list, list).
    """

    valid_records = []
    rejected_lines = []
    try:
        with open(path, "r") as file:
            for line in file:
                if line.strip() == "":
                    continue
                try:
                    result = parse_line(line)
                    if validate_record(result):
                        valid_records.append(result)
                    else:
                        rejected_lines.append(line)
                except MalformedRecordError:
                    rejected_lines.append(line)
    except FileNotFoundError:
        return [], []

    return valid_records, rejected_lines

    

            
            



def save_archive(path, records):
    """Write every record to `path` as CSV, one per line, no header.

    Field order is FIELD_NAMES. The file is overwritten, not appended to.

    Returns None.
    """
    with open(path, "w") as file:
        commas = 0
        temp = ""
        for i in range(len(records)):
            if(records[i] == ','):
                commas += 1
                file.write(f"{s},")
                s = ""
            match commas:
                case 0:
                    s += records[i]
                case 1:
                    s += records[i]
                case 2:
                    s += records[i]
                case 3:
                    s += records[i]
                case 4:
                    s += records[i]
        


            

    raise NotImplementedError("save_archive")
