s = "abcdabcd" #字串
d = {} #字典
for c in s:
  if c in d:
    d[c] = d[c] + 1
  else:
    d[c] = 1
  print('現在讀到的字母' , c, "字典變成", d)