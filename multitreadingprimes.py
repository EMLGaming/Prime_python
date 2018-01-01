from datetime import datetime
import time
from threading import Thread
print(datetime.now())
start_time = datetime.now()
one_minute = datetime.now()
timeout = time.time() + 60*5
highest = 1

input("Press enter to start:")
def thread0():
   for num in range(1,1000000000,7):
      if num > 1:
          for i in range(2,num):
              if (num % i) == 0 or time.time() > timeout:
                  break
          else:
              print("thread0: %s" % (num))
def thread1():
    for num1 in range(3,10000000,7):
      if num1 > 1:
          for i in range(2,num1):
              if (num1 % i) == 0 or time.time() > timeout:
                  break
          else:
              print("thread1: %s" % (num1))
def thread2():
   for num2 in range(5,10000000,7):
      if num2 > 1:
          for i in range(2,num2):
              if (num2 % i) == 0 or time.time() > timeout:
                  break
          else:
              print("thread2: %s" % (num2))
def thread3():
    for num3 in range(7,1000000000,8):
      if num3 > 1:
          for i in range(2,num3):
              if (num3 % i) == 0 or time.time() > timeout:
                  break
          else:
              print("thread3: %s" % (num3))
def threadcheck():
    while true:
      print("#######" + highest)
      if highest < num:
         highest = num
      if highest < num1:
         highest = num1
      if highest < num2:
         highest = num2
      if highest < num3:
         highest = num3
def end():
   if one_minute == daytime.now() + 1 :
      print("#"*60)
      print("The biggest prime is: %s" % (num))
      print("#"*60)
      stop_time = datetime.now()
      timeduration = stop_time - start_time
      print(datetime.now())
      print("It took: %s " % (timeduration))

#if name == 'main':
Thread(target = thread0).start()
Thread(target = thread1).start()
Thread(target = thread2).start()
Thread(target = thread3).start()
#Thread(target = threadcheck).start()
#Thread(target = end).start()
