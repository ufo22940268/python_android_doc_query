#!/usr/bin/python
import sys
import provider

allowed_params = []
def init():
    global allowed_params
    allowed_params = ["-m"]

def print_help():
    print "error:", "".join([x + " " for x in sys.argv])
    print '''Usage: androiddoc.py <options>

    <options>
        -q          The key word you want to query.'''

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

    params = {}
    for i in range(1, len(argv), 2):
        try:
            if argv[i] in allowed_params: 
                if is_value_valide(argv[i + 1]):
                    params[argv[i]] = argv[i + 1] 
                else:
                    return None
            else:
                return None
        except IndexError:
            return None
    if params == {}:
        return None
    else:
        return params

if __name__ == '__main__':
    init()
    params = compile_args()
    if params == None:
        print_help()
    else:
        print params

    url = provider.query_url_with_keyword()
