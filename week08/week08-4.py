a = 1234
ans = 0  #答案,要把撥下來的皮,慢慢塞進去
while a>0:
  ans = ans *10 +a%10
  print( '現在的a是', a, '撥出來的皮%10是', a%10, '現在的ans就變成', ans)
  a = a // 10