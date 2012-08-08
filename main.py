#!/usr/bin/python
import sys
import provider
import os

def print_help():
    print "error:", "".join([x + " " for x in sys.argv])
    print '''Usage: androiddoc.py [keywords]'''

def is_value_valide(str):
    if str == "":
        return False
    elif str[0] == "-":
        return False
    else:
        return True

def compile_args():
    argv = sys.argv
    if len(argv) <= 1:
        return None
    else:
        return argv[1]

def prompt(urls):
    keys = urls.keys()
    prompt = ""
    for i, v in zip(range(len(urls)), keys):
        prompt +=  "\t[{0}]:\t{1}\n".format(str(i), v)
    index = 0
    prompt +=  "Which one(input the index number):\n"
    while True:
        line = raw_input(prompt)
        if line.isdigit():
            index = int(line)
            break
    open(urls[keys[index]])

def get_prg():
    '''TODO Open with xdg-open if the os isn't mac,
        so webbrowser won't open on windows platform'''
    if sys.platform == "darwin":
        return "open"
    else:
        return "xdg-open"

def open(url):
    os.system(get_prg() + " " + url)

if __name__ == '__main__':
    key = compile_args()
    if key == None:
        print_help()

    urls = provider.query_url_with_keyword(key)
    prompt(urls)
