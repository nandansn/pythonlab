def missing_char(str, n):
  str = str[0:n] + str[n+1:len(str)]
  return str


print(missing_char("nanda",0))
