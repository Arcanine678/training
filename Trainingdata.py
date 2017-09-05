#!/usr/bin/env python

import sys
import os
from random import randint
import time
import random
import hashlib

num = 0;
while(1):
	os.system("echo " + hashlib.sha256(str(num)).hexdigest() + " >> trainingdata.txt");
	os.system("git add . && git commit -m 'training no: " + str(num) + "' && git push -u origin master");
	num = num + 1;
	print(num);
	time.sleep(randint(90,120);
	

