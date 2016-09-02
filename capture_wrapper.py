#!/usr/bin/env python

import sys
import subprocess

WIRESHARK = "/usr/bin/wireshark"

if len(sys.argv) == 2:
	interface = sys.argv[1].split("/")[-1]
	subprocess.call(["/usr/bin/wireshark", "-i", interface, "-k"])
else:
	print "error"


