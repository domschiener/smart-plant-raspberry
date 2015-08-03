#!/usr/bin/env python

"""
This program opens multiple process for us to be able to run twitter.py and getdata.py simultaneously.
Base code and influence from: skrrgwasme on Stackexchange
"""
import multiprocessing
import cgi
import os
import os.path
import signal

import twitter
import getdata

print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "</head>"
print "<body>"

processes = []
form = cgi.FieldStorage()

print "Welcome to the Smart Plant Program."

def abort():
    f = open('RUNNING.txt', 'r')
    process = f.readline()
    process = filter(None, process.split(","))
	
    for p in process:
        os.kill(int(p), signal.SIGQUIT)
	
    f.close()
    os.remove('RUNNING.txt')
		
def main():
    if not os.path.isfile("RUNNING.txt"):
        f = open('RUNNING.txt', 'w+')
	
        for func in [twitter.main, getdata.main]:
            processes.append(multiprocessing.Process(target=func))
            processes[-1].start()

        for p in processes:
            f.write(str(p.pid))
            f.write(",")
        f.close()

        choice = raw_input("Press X to abort all processes: ")
        if choice == "X":
            abort()
    else:
        print "Processes already operational."
        if form.getvalue('offline') == "True":
            abort()
	
if __name__ == '__main__':
	main()
	

print "</body>"
print "</html>"
