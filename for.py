import time

for i in range(0,3600):
   if i%2==0:
      print(i,'hello,world!')
   else:
      print(i,'goodbye,world')
   time.sleep(1)