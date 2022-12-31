print("""
      Hesap Makinesi Uygulaması

      """)
class Calc(object):
    
    def __init__(self, a, b):
        self.value1=a
        self.value2=b
        
    def add(self):
        return self.value1+ self.value2
    
    def multiply(self):
         return  self.value1 * self.value2
     
    def division(self):
         return  self.value1 / self.value2

print("choose add(1), multipy(2), divison(3)")
selection= input("select 1 or 2 or 3")

v1=int(input("first value"))
v2=int(input("second value"))
c1=Calc(v1, v2)
if selection=="1":
    add_result=c1.add()
    print("Add: {}".format(add_result) )       
elif selection=="2":
    multiply_result=c1.multiply()
    print("Multiply: {}".format(multiply_result) )   
elif selection=="3":
    division_result=c1.division()
    print("division: {}".format(division_result) )           
else:
    print("error")
      #%%
print("""
    Rastgele sayı Tahmin Oyunu

      """)
import random
import time

rastgele=random.randint(1, 40)
hak=7
while True:
   
    tahmin=int(input("tahmin:"))
    
    if(tahmin<rastgele):
        print("bekle")
        time.sleep(1)
        
        print("daha yüksek sayı söyleyiniz")
        hak-=1
        
    elif(tahmin>rastgele):
        print("bekle")
        time.sleep(1)
        
        print("daha düşük sayı söyleyiniz")
        hak-=1
    else:
        print("bekle")
        time.sleep(1)
        print("bildiniz",rastgele)
        break
    if (hak==0):
        print("hak bitti")
        print("sayi:",rastgele)
        break

      
      #%%
print("""
       Asal Sayı Kontrol 

      """)
i=2
def asalsayi(sayi):
   if(sayi==1):
       return False
   elif(sayi==2):
       return True
   else:
       for i in range(2,sayi):
           if(sayi%i==0):
               return False
           return True
while True:

    sayi=input("sayi")
    
    if (sayi=="q"):
        break
    else:
        sayi=int(sayi)
        if(asalsayi(sayi)):
              print(sayi,"asal")
        else:
            print(sayi,"değil")
  #%%
print("""
       Bir Sayının Tam Bölenlerini Bulma 

      """)

def bulma(sayi):
    tam_bolenler=[]
    for i in range(2,sayi):
        if(sayi%i == 0):
            tam_bolenler.append(i)
    return tam_bolenler
while True:

    sayi=input("sayi")
    
    if (sayi=="q"):
        break
    else:
        sayi=int(sayi)
        print("tam bölenler:", bulma(sayi))
