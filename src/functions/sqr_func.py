#coding=gb2312
from math import inf

def Normal():
  while True:
    n=input('输入一个数(正实数)：(q退出)\n')
    try:
      print('你输入的数的平方是',float(n)**2)
    except:
      if n=='q':
        break
      else:
        print('?')
        continue
def Sum():
  while True:
    num_serial=0
    b=-inf
    c=inf
    quadratic_sum=0
    restart=0
      
    a=input('请输入等差数列起始数(正整数)：(q退出)\n')
    restart=0
    if a.isdigit():
      a=int(a)
    else:
      if a=='q':
        break
      else:
        print('?')
        continue
    while b<a:
      b=input('请输入等差数列终止数(正整数)：(q退出)\n')
      restart=0
      if b.isdigit():
        b=int(b)
        if b<a:
          print('终止数要小于起始数.')
          continue
      else:
        if b=='q':
          break
        else:
          print('?')
          restart=1
      if restart==1:
        break
        
      while c>(b-a):
        c=input('请输入等差数列步长(正整数)：(q退出)\n')
        restart=0
        if c.isdigit():
          c=int(c)
          if c>(b-a):
            print('步长要小于终止数与起始数的差.')
            continue
        else:
          if c=='q':
             break
          else:
             print('?')
             restart=1
        if restart==1:
          break


        for num in range(a,b+1,c):
          num_serial+=1
          quadratic_sum+=(num**2)
          print('第',num_serial,'个数',num,'的平方为',num**2,'.')
        print('这些数的和为',quadratic_sum,'.\n')
        break
      break
