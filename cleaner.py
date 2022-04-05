from ast import While
import glob
import sys
import os
import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


address=sys.argv[1]
days=sys.argv[2]
files=glob.glob(address+"/*")
#while True:
for x in files:
        lastmod=time.ctime(os.path.getmtime(x))
        lastmod=datetime.datetime.strptime(lastmod, "%a %b  %d %X %Y")

        print(lastmod)
        end_date = lastmod + datetime.timedelta(days=10)
        print(end_date)
