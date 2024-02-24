import random
with open("a.txt", "w+") as f:
  f.write(str(random.randint(1, 2**32-1)))
