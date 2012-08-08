import db

prefix = ""

def read_prefix():
    global prefix
    if prefix != "":
        return prefix

    line = open("config", "r").readline().rstrip()
    try:
        return line.split("=")[1];
    except:
        print "Something wrong with config file.", sys.exc_info[0]
        raise

def init():
    global prefix
    prefix = read_prefix()

def compose(url):
    return prefix + url;

def query_urls(key):
    conn = db.connect()
    c = conn.cursor()
    c.execute("select link, label from data where lower(label) like '%{0}%'".format(key.lower()));

    urls = {}
    row = c.fetchone()
    while row != None:
        full_url = compose(row[0])
        label = row[1]
        urls[label] = full_url
        row = c.fetchone()
    return urls

def query_url_with_keyword(key):
    init()
    db_urls = query_urls(key)
    return db_urls

if __name__ == '__main__':
    query_url_with_keyword("textview")
