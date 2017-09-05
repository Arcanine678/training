#!/usr/bin/env python

import sys
import os
import time
import random
import hashlib

num = 0;
while(1):
	os.system("echo " + hashlib.sha256(str(num)).hexdigest() + " >> trainingdata.txt");
	#os.system("git add . && git commit -m 'training no: " + str(num) + "' && git push -u origin master");
	num = num + 1;
	time.sleep(5);
	

