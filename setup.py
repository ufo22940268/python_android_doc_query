#!/usr/bin/python
import os
import sys
import os.path

def init_cmds():
    return ["install"]

def print_help():
    print '''Ussage: ./setup.py [COMMANDS]

    COMMANDS:
                install:        install androiddoc app.'''

def invalied_argv(cmds):
    try: 
        if sys.argv[1] in cmds:
            return False
    except:
        return True
    return True

def install():
    os.system("tar -xvf docs.tar")
    os.system("rm docs.tar")
    print ("install successfully!");

def check_status():
    if not os.path.exists("./docs.tar"):
        print "installed already."
        exit(0)

if __name__ == '__main__':
    check_status()
    cmds = init_cmds()
    if invalied_argv(cmds):
        print_help()
        exit(-1)

    if sys.argv[1] == "install":
        install()
