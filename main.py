import time
x = 0
while not x == 51:
  time.sleep(.1)
  print(x)
  x += 1
x = 0
input('Proceed to infinite loop')
while True:
  print('INFINITE LOOP %s' % (x))
  x += 1