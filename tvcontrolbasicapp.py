print("""
      Televizyon Uygulaması

      """)
import random
import time
class Kumanda():
    
    def __init__(self, tv_durum ="kapalı",tv_ses=0,kanal_listesi=["trt"],kanal="trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_ac(self):
            if(self.tv_durum=="açık"):
                print("televizyon açık")
            else:
                print("televizyon açılıyor")
                self.tv_durum="açık"
    def tv_kapat(self):
            if(self.tv_durum=="kapalı"):
                print("televizyon kapalı")
            else:
                print("televizyon kapanıyor")
                self.tv_durum="kapalı"
    def ses_ayarlari(self):
        while True:
            cevap=input("ses azaltmak için < tıuşuna basın\n sesi artıır > \n çıkış")
            if(cevap=="<"):
                if(self.tv_ses!=0):
                    self.tv_ses -= 1
                    print("ses:", self.tv_ses)
            elif(cevap==">"):
                if(self.tv_ses!=32):
                    self.tv_ses+=1
                    print("ses:", self.tv_ses)
            else:
                  print("ses güncellendi")
                  break
    def kanal_ekle(self, kanal_ismi):
            print("kanal ekleniyor")
            time.sleep(1)
            self.kanal_listesi.append(kanal_ismi)
            print("kanal eklendi")
    def rastgele_kanal(self):
            rastgele=random.randint(0, len(self.kanal_listesi)-1)
            
            self.kanal=self.kanal_listesi[rastgele]
            
            print("şu anki kanal", self.kanal)
    def __len__(self):
            return len(self.kanal_listesi)
    def __str__(self):
            return "tv durumu {}\n tv ses {} \n kanal listesi{}\n şu anki kanal{}\n".format(self.tv_durum, self.tv_ses, self.kanal_listesi,self.kanal)

kumanda=Kumanda()
print("""
      
        Televizyon Uygulaması
      
      1.Tv Aç
      2.Tv Kapat
      3.Ses Ayarları
      4.kanal ekle
      5.kanal sayısını öğrenme
      6.rastgele kanala geçme
      7.televizyon bilgileri
      çıkmak için qya basın
      
      """
    )

while True:
    işlem=input("işlemi seçiniz")
    if (işlem=="q"):
        print("çıkılıyor")
        break
    elif(işlem=="1"):
        kumanda.tv_ac()
    elif(işlem=="2"):
        kumanda.tv_kapat()
    elif(işlem=="3"):
         kumanda.ses_ayarlari
    elif(işlem=="4"):
        kanal_isimleri=input("kanal isimlerini virgül ile ayırarak giriniz:")
        kanal_listesi=kanal_isimleri.split(",")
        
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif(işlem=="5"):
        print("kanal sayısı:", len(kumanda))
    elif(işlem=="6"):
        kumanda.rastgele_kanal()
    elif(işlem=="7"):
        print(kumanda)
    else:
        print("geçersiz işlem")
        
    
            
         
