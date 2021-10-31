import string 
import random

while True:
  int(nums=random.choice(string.digits))
  print(random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(nums))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27)))
