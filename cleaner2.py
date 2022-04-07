import glob
import sys
import os
import time
import datetime
import logging

def deletefile(address,day ):
    logging.basicConfig(filename="cleaner.log", level=logging.INFO)
    files=glob.glob(address+"/*", recursive=True)
    for x in files:
                if os.path.isdir(x):
                   deletefile(x,day) 
                lastmod=time.ctime(os.path.getmtime(x))
                lastmod=datetime.datetime.strptime(lastmod, "%a %b  %d %X %Y")
                if lastmod< datetime.datetime.now()-datetime.timedelta(days=int(day)):
                        logging.info(f':{datetime.datetime.now()}: {x} will be removed')
                        os.remove(x)
                else :
                        pass


try:
        address="C:\Users\Doruk\Desktop\Yeni klasör"
        day=2
        deletefile(address,day)        
except:
        print("Parametre hatası")