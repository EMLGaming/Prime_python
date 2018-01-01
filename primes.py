from datetime import datetime
import time
print(datetime.now())
start_time = datetime.now()
timeout = time.time() + 60*5
for num in range(1,179424692):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0 or time.time() > timeout:
               break
       else:
           print("prime: %s" % (num))
print("#"*60)
print("The biggest prime is: %s" % (num))
print("#"*60)
stop_time = datetime.now()
timeduration = stop_time - start_time
print(datetime.now())
print("It took: %s" % (timeduration))
