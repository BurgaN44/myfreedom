#def divis(a, b):
#   try:
#       print(a / b)
#   except ZeroDivisionError:
#       print('Не дели на ноль')
#  finally:
#       print('thats all')



def tnt(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('На ноль делить нельзя')
tnt(1,0)


#2
def division(lst):
    s = 0
    for i in lst:
        try:
            s += 1
        except Exception:
            pass
        print(s)
division([1,2,'str',12,14])

#3
def division_2(a):
    try:
        print(int(a))
    except Exception:
        print('Не могу это сделать')
division_2('0')