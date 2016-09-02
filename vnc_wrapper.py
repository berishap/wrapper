#!/usr/bin/env python

import sys
import subprocess


if len(sys.argv) == 2:
	print sys.argv[1][6:]
else:
	print "error"

subprocess.call(["/usr/bin/vncviewer", sys.argv[1][6:]])
