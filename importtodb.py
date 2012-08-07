import re
import db

def parse_line(line):
    d = {}
    m = re.match(".*id:(\d+).*label:\"([^\"]+)\".*link:\"([^\"]+)\".*type:\"([^\"]+)\".*"
            , line)
    d["id"] = m.group(1)
    d["label"] = m.group(2)
    d["link"] = m.group(3)
    d["type"] = m.group(4)
    return d

def write_to_db(data):
    conn = db.connect()
    for row in data:
        conn.execute("insert into data(id, label, link, type) values(?, ?, ?, ?)",
                (row["id"], row["label"], row["link"], row["type"]));
    conn.commit()
    conn.close()

if __name__ == '__main__':
    file = open("data.js", "r")
    data = []
    line = file.readline().rstrip()
    while line != "":
        data.append(parse_line(line))        
        line = file.readline().rstrip()
    write_to_db(data)
