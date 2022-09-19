def fibonacci(x,y):
  
  i = 0
  f = 0

  while (len(str(f)) != 1000):
    
    f = x + y
    x = y
    y = f

    i += 1

  print(len(str(f)))

  return f

x = 0
y = 1

print(fibonacci(x,y))
