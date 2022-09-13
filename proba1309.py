class SomeClass():
       def method1(self,x):
        a=int(input('Ievadiet pirmo koeficientu: '))
        b=int(input('Ievadiet otro koeficientu: '))
        c=int(input('Ievadiet trešo koeficientu: '))  
        return a*x*x-b*x-c

obj=SomeClass()
print(obj.method1(int(input('Ievadiet skaitli: '))))