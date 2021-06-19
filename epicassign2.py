# NAME AGE FUNCTION:
def str_spaces(fstring,sstring):
    print(fstring + ' ' + sstring)

mstring = input()
nstring = input()
str_spaces(mstring,nstring)


def nage(string,string2):
    print(string,end=' ')
    print(string2,end='')

nstr = input()
astr = input()
nage(nstr,astr)



#REVERSE STRING 39:
def revstr(fstring):
   string =''
   for i in fstring:
        string = i + string
   print(string)
mstring = input()
revstr(mstring)

def revstr(fstring):
   string =''
   for i in range(1,len(fstring)+1):
        string = string + fstring[len(fstring)-i]
   print(string)
mstring = input()
revstr(mstring)



# SQUARE RECTANGLE:
def squrec(length,breadth):
    if length == breadth:
        print('Yes')
    else:
        print('No')

lrec = int(input())
brec = int(input())

squrec(lrec,brec)



#VBIT EMPLOYEE
def bonus(sal,year):
   if year > 5:
     sal = int(sal*(5/100))
     print(f'Bonus is {sal}')
   else:
        print("No Bonus")

salary = int(input())
syears = int(input())
bonus(salary,syears)




#MULTIPLICATION TABLE
def multiples(multi):
  n = 1
  while n<=10:
      print(multi*n)
      n = n+1
mul = int(input())
multiples(mul)


