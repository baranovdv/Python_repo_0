# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
from decimal import Decimal
import random
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    f = "ADSDSDSDSD"

    n = [2,6]
    # f = f.replace('DS','spam',1)
    # d = bytearray(f,'utf-8')
    # help(f.replace)
    # print(dir(n))

    # M = [[1,2,3],[4,5,6],[7,8,9]]
    # col2 = [x[1] for x in M]
    # print(col2)
    # col2 = list(range(5))
    # col2 = [[x,x ** 2,x+444] for x in range(-3,3,1)]
    # print(col2)

    # def count_substring(string, sub_string):
    #     counter = 0
    #     for i in range(len(string)):
    #         if string.count(sub_string, i, i + len(sub_string)) == 1:
    #             counter += 1
    #     return counter

    # tuple = (('subfirst','subsecond'),'second','third','second')
    # print(tuple[2])
    # set = {'first','second','firste'}
    # print(set)

    dictionary = {'name':{'onre':['two','three']}, 'sur': ['surname','cra'], 'alpha':['beta'],'mess':['here ']}
    # print(dictionary)
    # KS = sorted(dictionary)
    # for key in KS:
    #     print(key + ':' + str(dictionary[key]))
    # S1 = set('ramtrre')
    # S2 = {'r','s','w'}
    # print(S1)
    # print(S2-S1)


    # class  Worker:
    #     def __init__(self,name,pay):
    #         self.name = name
    #         self.pay = pay
    #     def Raisepay(self,percent):
    #         self.pay = self.pay*(1+percent*0.01)
    #         print(self.pay)
    #
    # Ivan = Worker('Ivanov',100500)
    # Ivan.Raisepay(50)
    # print(Ivan.name)

    l = [1,2,3,4]
    l1 = [5,6]
    l.append(l1)
    print(l)
    l.extend(l1)
    print(l)
    x = '0.1'
    print(Decimal(x))
    # print(int('0.1')+0.1+0.1+0.1-0.4)
    # keys = list(dictionary.keys())
    # print(keys)

    # print('drink {x} vodka '.format(x=4))
    #
    # LL = ['first', 'second', 'third', 'forth']
    # random.shuffle(LL)
    # print(LL)
    # i=0
    L=[]
    # for i in range(3):
    #     name = input('Enter name ')
    #     score = input('Enter score ')
    #
    #     L.append([name,score])

    # E = ['3','5']
    # print(E)
    #
    # def func1(a):
    #     return int(a)
    #
    # print(set(map(func1, E)))

    E = '33 c 52'
    E.split(' ')
    print(E, type(E))

    print('saa %s %d' %('d',1))

    # a = 'r'
    # print(a)
    # b = a
    # print(b)
    # b = b + 'ss'
    # print(a,b)
    #
    # La = [1,2,3,4]
    # Lb = La[:]
    # print(La,Lb)
    # Lb[1] = 'ssdsd'
    # print(La,Lb)
    #
    # Ta = (1,2,3,4)
    # Tb = Ta
    # print(Ta,Tb)
    # Ta += ('ssdsd','sd')
    # print(Ta,Tb)
    #
    # Ta = {13,23,33,43}
    # Tb = Ta
    # print(Ta,Tb)
    # Ta = [1,2]
    # print(Ta,Tb)



    # print(L)
    # D = {}
    #
    # for v in range(0, len(L)):
    #     D[L[v][0]] = (L[v][1])
    #
    # print(D)
    #
    # DS = D.keys()
    # print(DS)

    # set = (sum(M[i]) for i in range(4))
    #
    # print(set)
    # s = next(set)
    # print(s)
    # se = next(set)
    # print(se)
    # M = [[x,x+1,x+2] for x in range(1,10,3)]
    # print(M)
    #
    # dict = {x:sum(M[x]) for x in range(3)}
    # print(dict)

    # exec(open('/Users/dmitrybaranov/PycharmProjects/pythonProject1/Test.py'))
    #! import Test
    # from Test import title
    # print(Test.title)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
