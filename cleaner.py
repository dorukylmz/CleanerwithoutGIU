import glob
import sys
import os
import time
import datetime

try:
        address=sys.argv[1]
        day=sys.argv[2]
        files=glob.glob(address+"/*")
        for x in files:
                lastmod=time.ctime(os.path.getmtime(x))
                lastmod=datetime.datetime.strptime(lastmod, "%a %b  %d %X %Y")
                if lastmod< datetime.datetime.now()-datetime.timedelta(days=int(day)):
                        print(f'{x} will be removed')
                        os.remove(x)
                else :
                        pass
except:
        print("Parametre hatası")