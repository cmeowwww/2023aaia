for i in range(1,10):
  for j in range(1,10):
    print(  i, 'x', j, '=', sep='', end='')
    if i*j<10: print(' ', sep='', end='')
    print( i*j,   sep='' , end='  ')        
  print()