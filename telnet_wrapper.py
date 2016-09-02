#!/usr/bin/env python

import sys
import subprocess

ROXTERM = "/usr/bin/roxterm"
KONSOLE = "/usr/bin/konsole"

if len(sys.argv) == 2:
	ip, port = sys.argv[1].strip("telnet://").split(":")
	subprocess.call([KONSOLE, "--new-tab", "-p", "tabtitle=%w", "-e", "telnet", ip, port])
	#subprocess.call([KONSOLE, "--new-tab", "-e", "telnet", ip, port])
else:
	print "error"


