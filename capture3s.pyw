#need if scr exactly same!

from PIL import ImageGrab
import time

import os


import threading
count = 0

def startTimer():
    global count
    timer = threading.Timer(3, startTimer)
    timer.start()
    #----------------------------do this here
    #capandsave()
    if capandsave_compare() == 1:
    
        print(count)
        count += 1
    else:
        print('skip')
    #----------------------------
    
##    if count > 5:
##        timer.cancel()
        


now = time.localtime()
datetime = "%04d-%02d-%02d-%02dh-%02dm-%02ds" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

dateonly = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)



def capandsave():
    now = time.localtime()
    datetime = "%04d-%02d-%02d-%02dh-%02dm-%02ds" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

    img=ImageGrab.grab()
    saveas="{}{}".format(datetime,'.jpg')
    img.save(saveas)

oldimg=0

def capandsave_compare():
    global oldimg
    now = time.localtime()
    datetime = "%04d-%02d-%02d-%02dh-%02dm-%02ds" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

    img=ImageGrab.grab()
    if not img == oldimg:
        
        #saveas="{}{}".format(datetime,'.jpg')
        files = os.listdir()
        nos=0
        while str(nos)+'.jpg' in files:
            nos += 1
            #print(nos)
        saveas="{}{}".format(nos,'.jpg')
        oldimg=img
        img.save(saveas)
        return 1
    
        
    else:
        return 0

    
try:
    os.mkdir(dateonly)
except:
    print('already is')


try:
    os.chdir(dateonly)
    print('moved')
except:
    print('coudundt moved')
    exit()


startTimer()
