from sqr_func import Normal,Sum

print('平方计算器  Date 2023.12.27')
num_serial=0


while True:
  mode=input('输入模式：(1：普通   2：平方和)\n')

  #平方计算   1
  if mode=='1':
    Normal()

  #平方和计算   2
  elif mode=='2':
    Sum()
  elif mode=="q":
    break
  #排除错误输入
  else:
    print('?')